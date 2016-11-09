import Blender
from Blender import Draw 
from Blender.BGL import *
import time
from Blender.Mathutils import *
import os
import thread
import math
from math import sin,cos

os.system('cls')
x1=200.0;y1=100.0
x2=400.0;y2=400.0
x3=600.0;y3=100.0
i=0
pt0=Vector(x1,y1);pt1=Vector(x2,y2);pt2=Vector(x3,y3)
radius=40
k1=(y2-y1)/(x2-x1);k2=(y3-y2)/(x3-x2);k3=(y3-y1)/(x3-x1)
cx1=x1;#cy1=y1;cx2=x2;cy2=y2
c=False;ca=False

	
def event(evt, val):
	if evt == Draw.ESCKEY :
		Draw.Exit()
		return


def changeI():
	global x1,y1,x2,y2
	if x1!=x2 and y1!=y2:
		first()
	time.sleep(0.1)	
	Draw.Redraw(1)


def first():
	global x1,y1	
	for i in range(5):
		x1+=float(i)
		y1+=float(i)*k1

def second():	
	global x2,y2,c
	for i in range(5):
		x2+=float(i)
		y2-=float(i)*(-k2)
	c=True

def third():	
	global c,x1,x3,y3
	if x3>cx1:
		for i in range(5):
			x3-=float(i)
			y3-=float(i)*k3
	c=True

def circleAB(i):
	global c
	glBegin(GL_LINE_LOOP)
	for i in range(51):
		a = 2.0*math.pi*float(i)/float(51) 
		dx=cos(a)*radius
		dy=sin(a)*radius
		glVertex2f((x1-radius/2)+dx,(y1+radius)+dy)
	glEnd()
	c=True
	
def circleBCe(i):
	if x2<=x3:
		glBegin(GL_LINE_LOOP)
		for i in range(51):
			a = 2.0*math.pi*float(i)/float(51) 
			dx=cos(a)*radius
			dy=sin(a)*radius
			glVertex2f((x2+radius)+dx,(y2+radius/3)+dy)		
		glEnd()
		second()

def circleCAe(i):
	global ca
	glBegin(GL_LINE_LOOP)
	for i in range(51):
		a = 2.0*math.pi *float(i)/float(51) 
		dx=cos(a)*radius
		dy=sin(a)*radius
		glVertex2f((x3)+dx,(y3-radius)+dy)
	glEnd()
	third()
	ca=True
	return ca

	"""def circleBC():
	global ca
	glBegin(GL_LINE_LOOP)
	for i in range(51):
		a = 2.0*math.pi *float(i)/float(51) 
		dx=cos(a)*radius
		dy=sin(a)*radius
		glVertex2f((x2)+dx,(y2+radius)+dy)
	glEnd()"""
	
def button_event(evt):  
	global radius
  	if evt == 1:			
		r=Draw.Create(radius)	
		block=[]			
		block.append(("R= ",r,0,600))
		retVal=Draw.PupBlock("Add radius",block) 
		radius = r.val
		Draw.Redraw(1)
		return

def gui():
	global x2,y2,radius     
	Draw.PushButton("Add point",1,1,10,100,70,"Add point to polygon")
	if (x1 > 0 and y1 > 0):
		glClearColor(1,1,1,1) 
	 	glClear(GL_COLOR_BUFFER_BIT) 
		glLineWidth(2)
		glColor3f(1.0,0,0)
		
		glBegin(GL_LINE_LOOP)
		glVertex2f(*pt0)	
		glVertex2f(*pt1)
		glVertex2f(*pt2)	
		glEnd()
		start()
		changeI()
		
def start():
	global c,x1,x2,y1,y2,i          
	
	if x1!=x2 and y1!=y2 and ca==False:
		circleAB(i)
		
	if x1==x2:
		c=False
		circleBC()
	if c==False:
		circleBCe(i)
	if c==False:
		circleCAe(i)
	
	
Draw.Register(gui, event,button_event)