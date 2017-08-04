#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#可变参数
#可变参数允许你传入0个或者任意个参数，这些可变参数在自动调用时自动组装为一个tuple
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum

print(calc(1,2,3))  #14
print(calc(*[1,2,3])) #14
print(calc(*(1,2,3))) #14


#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**hh):
	print('name:',name,'age:',age,'other:',hh)

#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：


person('coldbreath',23,city='wuhan',job='Engineer')
#name: coldbreath age: 23 other: {'job': 'Engineer', 'city': 'wuhan'}


#关键字参数有什么用
#拓展函数的功能，可以接收除必填参数外更多的参数
#可以先预装一个dict,然后，把该dict转为关键字参数传进去
extra = {'city':'shanghai','job':'engineer'}
person('胡有明','23',city=extra['city'],job=extra['job'])
#简化版
person('胡有明','23',**extra)
#name: 胡有明 age: 23 other: {'job': 'engineer', 'city': 'shanghai'}


#命名关键字参数
#来限制关键字参数的名字，例如只接收city和job作为关键字参数：
def person2(name,age,*,city,job):
	print(name,age,city,job)

person2('胡有明',22,city='jiangsu',job='engineer')
#胡有明 22 jiangsu engineer

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不需要一个特殊分隔符*了：
def person3(name,age,*args,city,job):
	print(name,age,args,city,job)

person3('coldbreath',22,1,2,3,city='gaungzhou',job='engineer')
#coldbreath 22 (1, 2, 3) gaungzhou engineer

#命名关键字可以有缺省值，从而简化调用
def person4(name,age,*,city='hangzhou',job):
	print(name,age,city,job)

person4('breathcold',25,job='advancedEngineer')
#breathcold 25 hangzhou advancedEngineer
#
#
#参数组合
#在python中定义函数，可以用必选参数，默认参数，可变参数，关键字参数，命名关键字参数u，这五种参数可以自由组合使用。但是参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=8,*,d,**kw):
	print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)


#递归函数
#在函数内部，可以调用其他函数。如果一个函数在内部调用其自身，这个函数卆递归函数
#举了例子，计算fact(n)=n!=1x2x3x4x...x(n-1)xn=(n-1)! x n=fact(n-1)xn
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
print(fact(4))
