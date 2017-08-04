#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
print('请输入一元二次方程的系数：')
a = float(input('输入a= '))
b = float(input('输入b= '))
c = float(input('输入c= '))

def quadratic(a,b,c):
	if not isinstance(a,(int,float)):
		raise TypeError('bad operand type')
	if not isinstance(b,(int,float)):
		raise TypeError('bad operand type')
	if not isinstance(c,(int,float)):
		raise TypeError('bad operand type')	
	d = b*b - 4*a*c
	if d >= 0 :
		x1 = (-b+math.sqrt(d)/(2*a))
		x2 = (-b-math.sqrt(d)/(2*a))
		print(x1,x2)
	elif d == 0:
		x1 = (-b)/(2*a)
		print(x1)
	else:
		print('无解')

quadratic(a,b,c)