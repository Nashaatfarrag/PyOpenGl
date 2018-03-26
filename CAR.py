from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
import time
def Init():
    #glOrtho(-10,10,-10,10,-10,10)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60,1,1.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glClearColor(1,1,1,1)
x=0
y=0
color = 0
co = -1
def draw():
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPopAttrib()
    glPopMatrix()


def Anime():
    global x,y,co,color
    time.sleep(.001)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)


    for i in range(-100,80, 10):
        glLoadIdentity()
        glColor(0, 0, 0)
        glScale(.5, 0.001, .2)
        glTranslate(i, 0, 0)
        glutSolidCube(4)
        #glFlush()
    glPopAttrib()
    glPopMatrix()


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glColor3f(1,0,0)
    glScale(1,.25,.5)
    glTranslate(x,0,0)
    glutWireCube(5)
    glLoadIdentity()
    glTranslate(x,5*.25,0)
    glScale(0.5,.25,0.5)
    glutWireCube(5)

##################
    glColor3f(0,0,0)

    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,2.5*.5)
    glRotate(y,0,0,1)
    glutWireTorus(.12,.4,12,8)

    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,-2.5*.65)
    glRotate(y,0,0,1)

    glutWireTorus(.12,.4,12,8)

    glLoadIdentity()
    glTranslate(x-2.25,-2.5*.25,2.5*.5)
    glRotate(y,0,0,1)
    glutWireTorus(.12,.4,12,8)

    glLoadIdentity()
    glTranslate(x-2.25,-2.5*.25,-2.5*.55)
    glRotate(y,0,0,1)

    glutWireTorus(.12,.4,12,8)

#################

    glColor3f(0,color+.5,1)
    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,0.1)
    glutSolidSphere(.25,10,40)

    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,-1)
    glutSolidSphere(.25,10,40)


    if(x > 15 ):
        x=-40

    x-=.02*co
    y+= .4*co

    if(color >=.5 and color >0):
        color += .5*co
    else:
        color += .5*co

    glPopAttrib()
    glPopMatrix()
    glColor(0,0,1)
    glScale(100, .001 , 4)
    glutWireCube(4)

    glFlush()



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"CAR")
Init()
glutDisplayFunc(Anime)
glutIdleFunc(Anime)
glutMainLoop()
