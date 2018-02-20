from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from OpenGL.GLUT import *
import numpy as np

def axis():
    glColor3d(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0, -1)
    glVertex2d(0, 1)
    glVertex2d(-1, 0)
    glVertex2d(1, 0)
    glEnd()


def cords():
    glColor3d(1, 0, 0)
    glBegin(GL_LINES)
    for i in np.arange(-1, 1.1, .01):
        glVertex2d(1, i)
        glVertex2d(-1, i)
    for j in np.arange(-1, 1.1, .01):
        glVertex2d(j, 1)
        glVertex2d(j, -1)
    glEnd()

def circle(r, x0, y0, s, R=1, G=1, B=1, t=1):
    if s == "L":
        glBegin(GL_LINE_LOOP)
        for i in np.arange(0, 2 * pi * t, 0.001):
            x = x0 + r * cos(i)
            y = y0 + r * sin(i)
            glVertex2d(x, y)
        glEnd()
    elif s == "P":
        glColor3d(R, G, B)
        glBegin(GL_POLYGON)
        for i in np.arange(0, 2 * pi * t, 0.01):
            x = x0 + r * cos(i)
            y = y0 + r * sin(i)
            glVertex2d(x, y)
        glEnd()


def rect(x, y, length, hight, R=1, G=1, B=1):
    glColor3d(R, G, B)
    glBegin(GL_POLYGON)
    glVertex2f(x, y)
    glVertex2f(x + hight, y)
    glVertex2f(x + hight, y + length)
    glVertex2f(x, y + length)
    glEnd()


def body():

    rect(-0.25, 0.30, 0.25, 0.5, 0.01, 0.84, 0.91)
    rect(-0.40, -0.30, 0.6, 0.8, 0.81, 0.04, 0.91)
    rect(-0.40, -0.65, 0.35, 0.2, 0.01, 0.84, 0.91)
    rect(0.20, -0.65, 0.35, 0.2, 0.01, 0.84, 0.91)
    rect(0.3, 0, 0.30, 0.15, 0.01, 0.84, 0.91)
    rect(-0.3-0.15, 0, 0.30, 0.15, 0.01, 0.84, 0.91)
    circle(.04, 0.15, .45, "P", 0.13, 0.45, 0.96)
    circle(.04, -0.15, .45, "P", 0.13, 0.45, 0.96)


def display():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    #cords()
    #axis()
    body()


    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Robot")
glutDisplayFunc(display)
glutMainLoop()