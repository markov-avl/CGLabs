from dataclasses import dataclass

try:
    import math
    import pygame
    from pygame.locals import *
except ImportError:
    print("PyRay could not import necessary modules")
    raise ImportError


# Closes the program
def close():
    pygame.display.quit()
    pygame.quit()


@dataclass
class Point:
    x: int | float
    y: int | float
    z: int | float


@dataclass
class Sphere:
    x0: int | float
    y0: int | float
    z0: int | float
    r: int | float

    def get_distance(self, point: Point) -> float:
        return abs(math.sqrt((self.x0 - point.x) ** 2 + (self.y0 - point.y) ** 2 + (self.z0 - point.z) ** 2)) - self.r


@dataclass
class Vector:
    i: int | float
    j: int | float
    k: int | float

    @property
    def length(self) -> int | float:
        return math.sqrt(self.i ** 2 + self.j ** 2 + self.k ** 2)

    def normalized(self):
        length = self.length
        return Vector(self.i / length, self.j / length, self.k / length)

    def dot_cos(self, vector) -> float:
        return (self.i * vector.i + self.j * vector.j + self.k * vector.k) / (self.length * vector.length)


def main():
    pygame.init()

    # Creates window
    WIDTH = 300
    HEIGHT = 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ray Marching")

    sphere = Sphere(WIDTH // 2, HEIGHT // 2, 400, min(WIDTH, HEIGHT) // 2)
    max_distance = 1
    phi = 0

    while True:
        screen.fill((25, 25, 25))

        light = Point(WIDTH // 2 + math.sin(phi) * 100, HEIGHT // 2 + math.cos(phi) * 100, 0)
        phi += 0.5

        for x in range(WIDTH):
            for y in range(HEIGHT):
                z = 0
                for _ in range(15):
                    distance = sphere.get_distance(Point(x, y, z))
                    if distance <= max_distance:
                        cos = Vector(light.x - x, light.y - y, light.z - z).dot_cos(
                            Vector(x - sphere.x0, y - sphere.y0, z - sphere.z0)
                        )
                        if cos < 0:
                            cos = 0
                        color = (int(255 * cos), int(255 * cos), int(255 * cos))
                        screen.set_at((x, y), color)
                        break
                    z += distance

        # Updating display
        pygame.event.pump()
        pygame.display.flip()


main()
