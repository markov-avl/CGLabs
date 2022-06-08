#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>

GLfloat xRotated = 1, yRotated = 1, zRotated = 1;
// Torus
GLdouble innerRadius = 0.5;
GLdouble outerRadius = 1;
GLint sides = 20;
GLint rings = 20;


void display() {
    // traslate the draw by z = -4.0
    // Note this when you decrease z like -8.0 the drawing will looks far , or smaller.
    glPushMatrix();

    glTranslatef(0.0, 0.0, -4.5);
    // Red color used to draw.
    glColor3f(0.8, 0.2, 0.1);
    // changing in transformation matrix.
    // rotation about X axis
    glRotatef(xRotated, 1.0, 0.0, 0.0);
    // rotation about Y axis
    glRotatef(yRotated, 0.0, 1.0, 0.0);
    // rotation about Z axis
    glRotatef(zRotated, 0.0, 0.0, 1.0);
    // scaling transfomation
    glScalef(1.0, 1.0, 1.0);
    // built-in (glut library) function , draw you a Torus.

    glMaterialf(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, 1.0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glTranslatef(0.0, 0.0, -2.25);
    glutWireTorus(innerRadius, outerRadius, sides, rings);

    glTranslatef(0.0, 0.0, 1.5);
    glutSolidTorus(innerRadius, outerRadius, sides, rings);

    glTranslatef(0.0, 0.0, 1.5);
    glutSolidTorus(innerRadius, outerRadius, sides, rings);

    glTranslatef(0.0, 0.0, 1.5);
    glutSolidTorus(innerRadius, outerRadius, sides, rings);

    glPopMatrix();

    glFlush();
}

void reshape(int w, int h) {
    glViewport(0, 0, (GLsizei) w, (GLsizei) h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if (w <= h)
        glOrtho(-1.5, 1.5, -1.5 * (GLfloat) h / (GLfloat) w,
                1.5 * (GLfloat) h / (GLfloat) w, -10.0, 10.0);
    else
        glOrtho(-1.5 * (GLfloat) w / (GLfloat) h,
                1.5 * (GLfloat) w / (GLfloat) h, -1.5, 1.5, -10.0, 10.0);
    glMatrixMode(GL_MODELVIEW);
    gluPerspective(40.0, (GLdouble) w / (GLdouble) h, 0.5, 20.0);
    glLoadIdentity();
}

void idle() {
    yRotated += -0.02;
    display();
}

void keyboard(int key, int x, int y) {
    if (key == GLUT_KEY_LEFT and rings > 5) {
        --sides;
        --rings;
        glutPostRedisplay();
    } else if (key == GLUT_KEY_RIGHT and rings < 50) {
        ++sides;
        ++rings;
        glutPostRedisplay();
    }
}

void init() {
    GLfloat mat_specular[] = {1.0, 1.0, 1.0, 1.0};
    GLfloat mat_shininess[] = {50.0};
    GLfloat light_position[] = {1.0, 1.0, 1.0, 0.0};
    glClearColor(0.0, 0.0, 0.0, 0.0);
//    glShadeModel(GL_SMOOTH);

    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess);
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);

    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_DEPTH_TEST);
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(1500, 500);
    glutInitWindowPosition(100, 100);
    glutCreateWindow(argv[0]);
    init();

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutIdleFunc(idle);
    glutSpecialFunc(keyboard);

    glutMainLoop();
    return 0;
}