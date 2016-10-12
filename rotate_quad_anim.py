# rotatingting  line
import os
import Blender
from Blender import Draw 
from Blender.BGL import *
import time
from Blender.Mathutils import *
import math
from math import sin,cos
import random

os.system('cls')

pt0=Vector(100,100); pt1=Vector(100,200); pt2 = Vector(200,200); pt3 = Vector(200,100) #
mddl=(pt0+pt2)*0.5
pt0s=pt0-mddl;pt1s=pt1-mddl;pt2s=pt2-mddl;pt3s=pt3-mddl
a = 0; s = 0; pl = 1.0; check = 1; col_b = 1.0; col_c = 1.0; zer_one = 0.1	
	
def changeA():
	global a,s,check
	s += .3	
	a +=- .3
	
	if s >= 1.5:
		s = 0
		check += 1
	#if a< -6: Draw.Exit() #1.5 eto 90 gradusov
	time.sleep(0.1)	
	Draw.Redraw(1)
	
	
def rotMatr(ang):
	mtr=Matrix([cos(ang),-sin(ang)],[sin(ang),cos(ang)])
	return mtr	
	
def event(evt, val):     
  if evt == Draw.ESCKEY :	
    Draw.Exit()         



def rand_s():
	global s, col_b, col_c	
	if s == 0:
		col_b = random.random()
		col_c = random.random()
		glColor3f(1.0,col_b,col_c)
	else:
		glColor3f(1.0,col_b,col_c)
	
def changesize():
	global check
	if check % 2:
		rez = bigquad()
	else:
		rez = smallquad()
	
	return rez 	

def diagMatr():
	mtr = Matrix([changesize(),0],[0,changesize()])
	return mtr

def bigquad():
	global pl
	pl += zer_one
	if pl >= 2:
		smallquad()
	return pl

def smallquad():
	global pl
	pl -= zer_one
	if pl <= 1.0:
		bigquad()
	return pl

def gui():              
	glClearColor(0,0,0,1) # background color
 	glClear(GL_COLOR_BUFFER_BIT) # clear image buffer
	rand_s()	
	mtr=diagMatr()	
	glLineWidth(5)
	mtr1=rotMatr(a)
	rpt0 = mtr*mtr1*pt0s
	rpt1 = mtr*mtr1*pt1s
	rpt2 = mtr*mtr1*pt2s
	rpt3 = mtr*mtr1*pt3s
	pt0t = rpt0+mddl
	pt1t = rpt1+mddl
	pt2t = rpt2+mddl
	pt3t = rpt3+mddl
	
	glBegin(GL_QUADS)
	glVertex2f(*pt0t) # access to coords	
	glVertex2f(*pt1t)	
	glVertex2f(*pt2t)	
	glVertex2f(*pt3t)	
	glEnd()	
	
	changeA()
	
Draw.Register(gui, event,None)