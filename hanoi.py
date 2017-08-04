#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# 重点其实是：不要一开始就关心每一步怎么解决的，你只需要把函数当成一个实现你目的的神器，随时调用。也就是递归。
# 现在有个n个盘子，a,b,c三个塔。
#把n个盘子抽象成两个盘子，n-1 和 底下最大的1
#move(N,起点，缓冲区，终点）
#N: 盘子的个数。
def move(n,a,b,c):
	if n==1:
		print(a,'->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

move(3,'A','B','C')