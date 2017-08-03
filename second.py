#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = []

n = 100
while n > 0 :
	l.append(n)
	n -= 1
#print(l)

#list,tuple操作方法
#1.切割
a = ['a','b','c']
#slice [0:2] 索引[0,2)
print(a[0:2]) #['a','b']
print(a[1:2]) #['b']

#倒数切片a[-1]取倒数第一个元素，a[-1:]倒数第一个的切片
print(a[-1:]) #c

b = list(range(100))
#取前10位数
print(b[:10])
#后10位数
print(b[-10:])
#前11到20
print(b[10:20])
#前10位每隔2
print(b[:10:2])
#所有数每5个取一个
print(b[::5])
#tuple也是一种list,不同的是tuple不可变
print((1,2,3,4,5)[:4]) #(1,2,3,4)
#str也是一种list，
print('abcdefg'[:5]) #abcde

c = list(range(10))
#岔开替换数量要与之对应
c[::2] = [55,55,55,55,55]
print(c)#[55, 1, 55, 3, 55, 5, 55, 7, 55, 9]

d = list(range(10))
d[1:2] = [11,12,13]
print(d)#[0, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

e = tuple(range(10))
e[1:2] = [] #[1,2,3,4] 
print(d)#TypeError: 'tuple' object does not support item assignment
