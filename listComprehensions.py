#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# 列表生成式，是Python中很简单但是很强大的创建list的生成式
# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
# 生成[1,2,3,,,10]
print(list(range(1,11))) 
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#生成[1x1,2x2,...10x10]
#for in 
r = []
for x in range(1,11):
	r.append(x*x)
print(r)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#生成式
print([x*x for x in range(1,11)])
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
#for 循环后面还可以加判断
print([x*x for x in range(1,11) if x % 2 == 0])
#[4, 16, 36, 64, 100]
#
#还可以使用两层循环，不过三层和三层以上就很少用到了
print([m+n for m in 'abc' for n in 'xyz'])
#['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']

#利用生成式，可以列出当前目录下所有文件和目录名
import os #导入os模块
print([d for d in os.listdir('.')]) #listdir可以列出文件和目录
#['.git', 'changeArgus.py', 'feature.py', 'first.py', 'hanoi.py', 'learning.py', 'listComprehensions.py', 'quadratic.py','second.py', 'test.py']

#for 循环其实可以同时写两个甚至多个变量

f = {'x':'a','y':'b','z':'c'}
for k,v in f.items():
	print(k,'=',v)

# z = c
# y = b
# x = a
# 
# 因此列表生成式也可以用两个变量来生成list
# 
print([k+'='+v for k,v in f.items()])
#['z=c', 'y=b', 'x=a']
#
#把一个list中所有字符串变成小写

g = ['ABC','CDE','baA',18,None]
print([x.lower() for x in g if isinstance(x,str)])
#['abc', 'cde', 'baa']
