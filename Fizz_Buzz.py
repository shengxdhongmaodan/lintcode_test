#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author  : shengxd
@Contact : 740693424@qq.com
@File    :   Fizz_Buzz.py
@Time    :   2019/11/5 18:53
@Desc    :
描述

给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：

如果这个数被3整除，打印fizz.
如果这个数被5整除，打印buzz.
如果这个数能同时被3和5整除，打印fizz buzz.
如果这个数既不能被 3 整除也不能被 5 整除，打印数字本身。
你是否可以只用一个 if 来实现
"""
import os

module = ""
case = "Fizz_Buzz"
# 列表推导式
res = [[[str(i), 'buzz'][ i%5==0], ['fizz', 'fizz buzz'][i%5==0]][i%3==0] for i in range(1,16)]
str_list = []
for i in range(1, 16):
    if i%3 == 0:
        if i%5 == 0:
            str_list.append('fizz buzz')
        else:
            str_list.append('fizz')

    else:
        if i % 5 == 0:
            str_list.append('buzz')
        else:
            str_list.append(str(i))


# if __name__ == "__main__":
