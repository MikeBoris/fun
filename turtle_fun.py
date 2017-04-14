"""
Fun with turtle graphics

usage: python turtle_fun.py
"""
import math
import random
from turtle import *

def randomTriangle():
	"""Draws random triangle"""
	# random pen width
	w = random.randint(2, 10)
	pen.width(w)
	# random pen color
	red = random.random()
	green = random.random()
	blue = random.random()
	pen.color(red, blue, green)
	# random points of triangle
	x1 = random.randint(-300, 300)
	y1 = random.randint(-300, 300)
	x2 = random.randint(-300, 300)
	y2 = random.randint(-300, 300)
	x3 = random.randint(-300, 300)
	y3 = random.randint(-300, 300)
	# lift pen to move to first point
	pen.penup()
	pen.setx(x1)
	pen.sety(y1)
	pen.pendown()
	# pen down for drawing
	pen.goto(x2, y2)
	pen.goto(x3, y3)
	pen.goto(x1, y1)

def randomCircle():
	"""Draws a random circle"""
	w = random.randint(2, 10)
	pen.width(w)
	red = random.random()
	green = random.random()
	blue = random.random()
	pen.color(red, green, blue)
	# set random origin
	x1 = random.randint(-300, 300)
	y1 = random.randint(-300, 300)
	# lift pen to move to origin and set origin coordinates
	pen.penup()
	pen.setx(x1)
	pen.sety(y1)
	# set down pen and draw circle of random radius length
	pen.pendown()
	radius = random.randint(10, 200)
	pen.circle(radius)

if __name__ == '__main__':
	pen = Pen()
	for i in range(10):
		randomTriangle()
		randomCircle()
