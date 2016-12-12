import math

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = dsquared**0.5
	return result
	
def areaOfCircle(r):
	b = math.pi * r**2
	return b
	
def area2(xc, yc, xp, yp):
	r = distance(xc, yc, xp, yp)
	result = areaOfCircle(r)
	return result
	
	
area2