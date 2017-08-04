#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def area_of_circle(r):
	pi = 3.14
	return pi*r**2

def sum2(start,end,func):
	total = 0
	for x in range(start,end):
		total += func(x)
	return total

def func1(x):
	return x

def func2(x):
	return x**2+1

print(area_of_circle(3))
print(sum2(1,11,func1))
print(sum2(1,101,func2))


#参数；类型检测
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

#my_abs("-6") #TypeError: bad operand type
print(my_abs(-6)) #6


#返回多个值
import math
def move(x,y,step,angle=0):
	nx = x + step*math.cos(angle)
	ny = y - step*math.sin(angle)
	return nx,ny

print(move(10,10,2,45)) #(11.05064397763546, 8.298192950931764) 就是一个tuple

print(list(range(1,101)))

l = []
n = 1
while n <= 100:
	l.append(n)
	n += 2
print(l)

