#迭代
#for in

#dict迭代 for in 默认以key迭代
#key迭代
#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

d = {'a':1,'b':2,'d':3}

for key in d:
	print(key)
# a
# d
# b

#value 迭代
for value in d.values():
	print(value)
# 1
# 3
# 2

#同时迭代
for item in d.items():
	print(item)

# ('a', 1)
# ('d', 3)
# ('b', 2)


#判断是否可迭代
from collections import Iterable
print(isinstance('abc',Iterable)) #True
print(isinstance([1,2,3],Iterable)) #True
print(isinstance(123,Iterable)) #False


#如果要对list实现类似Java那样的下标循环怎么办？
#Python内置的enumerate函数可以把一个list变成索引-元素对，
#这样就可以在for循环中同时迭代索引和元素本身

for i,value in enumerate(['a','b','c']):
	print(i,value)

# 0 a
# 1 b
# 2 c

#for循环里面同时引入两个变量
for x,y in [(1,1),(2,2),(3,3)]:
	print(x,y)

# 1 1
# 2 2
# 3 3
# 
#for 循环其实可以同时写两个甚至多个变量

f = {'x':'a','y':'b','z':'c'}
for k,v in f.items():
	print(k,'=',v)

# z = c
# y = b
# x = a


















