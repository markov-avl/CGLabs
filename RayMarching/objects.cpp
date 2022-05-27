#include <glm/glm.hpp>
#include <glm/vec2.hpp>
#include <glm/vec3.hpp>


struct Point {
    float x;
    float y;
    float z;
};


struct Object {
    float x0;
    float y0;
    float z0;

    Object(float x0, float y0, float z0) {
        this->x0 = x0;
        this->y0 = y0;
        this->z0 = z0;
    }

    virtual float getDistance(const Point &point) = 0;

    glm::vec3 getVectorFromPointToCenter(const Point &point) {
        return glm::vec3(x0 - point.x, y0 - point.y, z0 - point.z);
    }
};


struct Sphere : public Object {
    float R;

    Sphere(float x0, float y0, float z0, float R) : Object(x0, y0, z0) {
        this->R = R;
    }

    float getDistance(const Point &point) {
        return glm::length(getVectorFromPointToCenter(point)) - R;
    }
};


struct Torus : public Object {
    float r;
    float R;

    Torus(float x0, float y0, float z0, float r, float R) : Object(x0, y0, z0) {
        this->r = r;
        this->R = R;
    }

    float getDistance(const Point &point) {
        glm::vec3 fromPointToCenter = getVectorFromPointToCenter(point);
        glm::vec2 p(R, r);
        glm::vec2 q(glm::length(glm::vec2(fromPointToCenter.x, fromPointToCenter.y)) - p.x, fromPointToCenter.z);
        return glm::length(q) - p.y;
    }
};


struct Cone : public Object {
    float h;

    Cone(float x0, float y0, float z0, float h) : Object(x0, y0, z0) {
        this->h = h;
    }

    float getDistance(const Point &point) {
        glm::vec3 fromPointToCenter = getVectorFromPointToCenter(point);
        glm::vec2 q = h * glm::vec2(1.125, -1.0);
        glm::vec2 w = glm::vec2(glm::length(glm::vec2(fromPointToCenter.x, fromPointToCenter.y)), fromPointToCenter.y);
        glm::vec2 a = w - q * glm::clamp(glm::dot(w, q) / glm::dot(q, q), 0.0f, 1.0f);
        glm::vec2 b = w - q * glm::vec2(glm::clamp(w.x / q.x, 0.0f, 1.0f), 1.0f);
        float k = glm::sign(q.y);
        float d = glm::min(glm::dot(a, a), glm::dot(b, b));
        float s = glm::max(k * (w.x * q.y - w.y * q.x), k * (w.y - q.y));
        return glm::sqrt(d) * glm::sign(s);
    }
};