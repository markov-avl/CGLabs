import numpy as np
from PIL import Image
from PIL.ImageDraw import Draw


def quad_as_rect(quad):
    return not (quad[0] != quad[2] or quad[1] != quad[7] or quad[4] != quad[6] or quad[3] != quad[5])


def quad_to_rect(quad):
    assert len(quad) == 8
    assert quad_as_rect(quad)
    return quad[0], quad[1], quad[4], quad[3]


def rect_to_quad(rect):
    assert len(rect) == 4
    return rect[0], rect[1], rect[0], rect[3], rect[2], rect[3], rect[2], rect[1]


# разбивает на части (сетка)
def griddify(xy: tuple[int, int, int, int], rows: int, colums: int, ):
    h = xy[3] - xy[1]
    w = xy[2] - xy[0]

    # шагаем (делим картинку по частям)
    x_step = w / colums
    y_step = h / rows

    y = xy[1]
    grid_vertex_matrix = []
    for _ in range(rows + 1):
        grid_vertex_matrix.append([])
        x = xy[0]
        for _ in range(colums + 1):
            grid_vertex_matrix[-1].append([int(x), int(y)])
            x += x_step
        y += y_step

    # разбили изображение на сетку
    grid = np.array(grid_vertex_matrix)
    return grid


# рандомизируем разбитые части на основе полученных (искажаем сетку)
def distort_grid(grid: np.ndarray, max_shift: int):
    new_grid = np.copy(grid)

    # находим границы рисунка
    x_min = np.min(new_grid[:, :, 0])
    y_min = np.min(new_grid[:, :, 1])
    x_max = np.max(new_grid[:, :, 0])
    y_max = np.max(new_grid[:, :, 1])

    # new_grid.shape - вернёт количество массивов, подмассивов, элеиентов в подмассивах
    new_grid += np.random.randint(- max_shift, max_shift + 1, new_grid.shape)
    new_grid[:, :, 0] = np.maximum(x_min, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.maximum(y_min, new_grid[:, :, 1])
    new_grid[:, :, 0] = np.minimum(x_max, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.minimum(y_max, new_grid[:, :, 1])
    return new_grid


def grid_to_mesh(src_grid, dst_grid):
    mesh = []
    for i in range(src_grid.shape[0] - 1):
        for j in range(src_grid.shape[1] - 1):
            src_quad = [src_grid[i, j, 0], src_grid[i, j, 1],
                        src_grid[i + 1, j, 0], src_grid[i + 1, j, 1],
                        src_grid[i + 1, j + 1, 0], src_grid[i + 1, j + 1, 1],
                        src_grid[i, j + 1, 0], src_grid[i, j + 1, 1]]
            dst_quad = [dst_grid[i, j, 0], dst_grid[i, j, 1],
                        dst_grid[i + 1, j, 0], dst_grid[i + 1, j, 1],
                        dst_grid[i + 1, j + 1, 0], dst_grid[i + 1, j + 1, 1],
                        dst_grid[i, j + 1, 0], dst_grid[i, j + 1, 1]]
            dst_rect = quad_to_rect(dst_quad)
            mesh.append([dst_rect, src_quad])
    return mesh


def draw_grid(image: Image, grid: np.ndarray) -> None:
    drawer = Draw(image)
    for x in range(grid.shape[0] - 1):
        for y in range(grid.shape[1] - 1):
            for dx in (0, 1):
                for dy in (0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    drawer.line((*grid[x][y], *grid[x + dx][y + dy]), fill='red')


if __name__ == '__main__':
    image = Image.open('source/image-2.png')
    rows = 5
    columns = 5

    grid = griddify((0, 0, image.width, image.height), rows, columns)
    image_with_grid = image.copy()
    draw_grid(image_with_grid, grid)
    image_with_grid.save('result/warping-before.png')

    distorted_grid = distort_grid(grid, 30)
    mesh = grid_to_mesh(distorted_grid, grid)

    correctly_distorted_grid = grid.copy()
    for i in range(correctly_distorted_grid.shape[0] - 1):
        for j in range(correctly_distorted_grid.shape[1] - 1):
            correctly_distorted_grid[i][j][0] += grid[i][j][0] - distorted_grid[i][j][0]
            correctly_distorted_grid[i][j][1] += grid[i][j][1] - distorted_grid[i][j][1]

    image_with_distorted_grid = image.transform(image.size, Image.MESH, mesh, Image.BILINEAR)
    draw_grid(image_with_distorted_grid, correctly_distorted_grid)
    image_with_distorted_grid.save('result/warping-after.png')
