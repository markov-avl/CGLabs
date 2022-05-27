#include <SFML/Graphics.hpp>
#include <glm/glm.hpp>
#include <glm/vec3.hpp>
#include "objects.cpp"


const short WINDOW_WIDTH = 300;
const short WINDOW_HEIGHT = 300;
const float MAX_DISTANCE = 0.5f;
const int LIGHT_STEP = 10;
const int RAY_MARCHING_STEP = 15;


glm::float64 dotCos(const glm::vec3 vec1, const glm::vec3 vec2) {
    return (vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z) / (glm::length(vec1) * glm::length(vec2));
}


sf::RenderWindow window(sf::VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), "Ray Marching");
sf::Texture pixels;
sf::Sprite sprite;

// Создаем необходимые объекты
Sphere sphere(
        static_cast<float>(WINDOW_WIDTH / 2),
        static_cast<float>(WINDOW_HEIGHT / 2),
        500,
        static_cast<float>(std::min(WINDOW_WIDTH, WINDOW_HEIGHT) / 2)
);
Point light{
        static_cast<float>(WINDOW_WIDTH / 2),
        static_cast<float>(WINDOW_HEIGHT / 2),
        0
};
Point scenePoint;
glm::vec3 fromLight, fromObject;


int main() {
    sf::Uint8 pixelData[WINDOW_WIDTH * WINDOW_HEIGHT * 4];
    pixels.create(WINDOW_WIDTH, WINDOW_HEIGHT);
    sprite.setTexture(pixels);

    // Окрашиваем фон в черный цвет
    for (unsigned int i = 0; i < WINDOW_WIDTH * WINDOW_HEIGHT * 4; ++i) {
        pixelData[i] = (i % 4 != 3) ? 20 : 255;
    }

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)) {
            light.x = light.x - LIGHT_STEP >= 0 ? light.x - LIGHT_STEP : 0;
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)) {
            light.x = light.x + LIGHT_STEP <= WINDOW_WIDTH ? light.x + LIGHT_STEP : WINDOW_WIDTH;
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
            light.y = light.y - LIGHT_STEP >= 0 ? light.y - LIGHT_STEP : 0;
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) {
            light.y = light.y + LIGHT_STEP <= WINDOW_HEIGHT ? light.y + LIGHT_STEP : WINDOW_HEIGHT;
        }

        // Собственно алгоритм рей марчинга
        for (unsigned int x = 0; x < WINDOW_WIDTH; ++x) {
            for (unsigned int y = 0; y < WINDOW_HEIGHT; ++y) {
                float z = 0;
                for (char i = 0; i < RAY_MARCHING_STEP; ++i) {
                    scenePoint = {static_cast<float>(x), static_cast<float>(y), z};
                    float distance = sphere.getDistance(scenePoint);

                    if (distance <= MAX_DISTANCE) {
                        fromLight = {light.x - x, light.y - y, light.z - z};
                        fromObject = {x - sphere.x0, y - sphere.y0, z - sphere.z0};

                        float cos = dotCos(fromLight, fromObject);
                        if (cos < 0.0f) {
                            cos = 0.0f;
                        }

                        unsigned int location = (y * WINDOW_WIDTH + x) * 4;
                        pixelData[location] = 200 * cos + 55;     // red
                        pixelData[location + 1] = 200 * cos + 55; // green
                        pixelData[location + 2] = 200 * cos + 55; // blue
                        break;
                    }

                    z += distance;
                }
            }
        }

        pixels.update(pixelData);
        window.draw(sprite);
        window.display();
    }

    return 0;
}