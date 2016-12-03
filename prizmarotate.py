'''
Color cube on base of plane
Implement MultMatrix
Camera looks at vertex
'''
import Blender
from Blender import Draw, BGL
from Blender.BGL import *
import time
import math
from math import sqrt
a=0
d=1
z=(3**0.5)*5
def changeA():
	global a
	global d
	a +=10
	d+=4
	time.sleep(0.1)
	Draw.Redraw(1)
def key(evt,val):
	if evt==Draw.ESCKEY: Draw.Exit()
def thiscube():
	glBegin(GL_QUADS)
	glVertex3f(-5,-5,0)
	glVertex3f(5,-5,0)
	glVertex3f(5,5,0)
	glVertex3f(-5,5,0)
	glEnd()
def myCube():
	glPushMatrix()
	glTranslatef(0,0,5)
	glColor3f(1,0,0)
	thiscube()
	glTranslatef(0,0,-10)
	glRotatef(180,0,1,0)
	glColor3f(0,1,0)
	thiscube()
	glPopMatrix()
	glPushMatrix()
	glRotatef(90,0,1,0)
	glTranslatef(0,0,5)
	glColor3f(0,0,1)
	thiscube()
	glTranslatef(0,0,-10)
	glRotatef(180,0,1,0)
	glColor3f(1,1,0)
	thiscube()
	glPopMatrix()
	glPushMatrix()
	glRotatef(90,1,0,0)
	glTranslatef(0,0,5)
	glColor3f(1,0,1)
	thiscube()
	glTranslatef(0,0,-10)
	glRotatef(180,1,0,0)
	glColor3f(0,1,1)
	thiscube()
	glPopMatrix()
def thisprizma():
	glBegin(GL_POLYGON)
	glVertex3f(-10,0,0)
	glVertex3f(-5,z,0)
	glVertex3f(5,z,0)
	glVertex3f(10,0,0)
	glVertex3f(5,-z,0)
	glVertex3f(-5,-z,0)
	glEnd()
def myPrizma():
	glPushMatrix()
	glTranslatef(0,0,5)
	glColor3f(0,1,0)
	thisprizma()
	glTranslatef(0,0,-10)
	glRotatef(180,0,1,0)
	glColor3f(0,1,0)
	thisprizma()
	glPopMatrix()
	glPushMatrix()
	glTranslatef(0,z,0)
	glRotatef(90,1,0,0)
	glColor3f(1,0,1)
	thiscube()
	glRotatef(180,1,0,0)
	glTranslatef(0,0,-2*z)
	thiscube()
	glPopMatrix()
	glPushMatrix()
	glColor3f(1,0,0)
	glRotatef(90,1,0,0)
	glRotatef(60,0,1,0)
	glTranslatef(0,0,z)
  	thiscube()
	glRotatef(180,0,0,1)
	glTranslatef(0,0,-2*z)
	thiscube()
	glColor3f(0,0,1)
	glPopMatrix()
	glPushMatrix()
	glRotatef(90,1,0,0)
	glRotatef(-60,0,1,0)
	glTranslatef(0,0,z)
	thiscube()
	glRotatef(180,0,0,1)
	glTranslatef(0,0,-2*z)
	thiscube()
	glPopMatrix()
def createScene():
	glPushMatrix()
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glRotatef(a,0,1,0)
	myPrizma()
	glPopMatrix()
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glRotatef(a,0,0,1)
	glTranslatef(25,1,-10)
	glRotatef(2*d,1,0,1)
	myCube()
	glPopMatrix()


def gui():
	glClearColor(0,0,0,1)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	glViewport(100,100,700,700)
	glPushMatrix()
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(-20,100,-20,100,-200,200)
	v1=1/sqrt(2)
	v2=1/sqrt(2)
	v3=v1*v2
	v4=v1/v2
	buf=Buffer(GL_FLOAT,16,[v3,v2,v1,0,v3,-v2,v1,0,-v4,0,v1,0,0,0,0,1])
	#glMultMatrixf(buf)
	glTranslatef(50,50,50)

	glMultMatrixf(buf)

	createScene()
	changeA()
Draw.Register(gui,key,None)