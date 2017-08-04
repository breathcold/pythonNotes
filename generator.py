#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# 列表生成器可以创建一个列表，但是收到内存限制，如果列表元素过多，会占用很大的存储空间
# 因此需要一种算法，可以在循环中不断推算后续的元素，这样就不必创建完整的list，从而节约大量空间

#创建一个生成器 generator
#方法一：把列表生成器的[]换成()
L = [ x*x for x in range(1,11)]
print(L)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

g = (x*x for x in range(1,11))
print(g)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#遍历拿数据,也可以通过next()拿，但是太变态了
for x in g:
	print(x)
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
#

#斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a,b=b,a+b
		n = n+1
	return 'done'
fib(10)

# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 
# 只要把print(b)换成yield b 就可以吧fib函数变成 generator

def generator(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b,a+b
		n = n+1
	return 'done'

print(generator(6))
#<function generator at 0x00000000006BE510>
for x in generator(6):
	print(x)
# 1
# 1
# 2
# 3
# 5
# 8
# 
#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

h = generator(6)
for x in h:
	while True:
		try:
			x = next(h)
			print('g ->',x)
		except StopIteration as e:
			print('generator return value',e.value)
			break
# g -> 1
# g -> 2
# g -> 3
# g -> 5
# g -> 8
# generator return value done