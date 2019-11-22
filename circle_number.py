#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author  : shengxd
@Contact : shengxd@huahuan.com
@File    :   circle_number.py
@Time    :   2019/11/21 15:16
@Desc    :
下面是来自某知名公司的一道“面试题”：给定 4，应该输出如下形式的数据：
01 12 11 10
02 13 16 09
03 14 15 08
04 05 06 07

给定 5，应该输出如下形式的数据：
01 16 15 14 13
02 17 24 23 12
03 18 25 22 11
04 19 20 21 10
05 06 07 08 09

仔细观察上面的试题，不难发现程序就是“绕圈圈”填入整数，如图 1 所示：


图 1 填数规则

掌握上面的规律之后，我们打算使用列表嵌套列表（相当于二维列表）的方式来存储这些整数，将数值存入嵌套列表时需要遵守这种“绕圈圈”的规则，然后再以二维方式将这个嵌套列表打印出来。

为了控制“绕圈”，该程序的关键点就是控制绕固的拐弯点。在图 1 中标出的对角线上的位置，就是重要的拐弯点。

找到图中 ①、②、③ 号转弯线之后，可以发现如下规则：
位于 ① 号转弯线的行索引与列索引总和为 n - 1（即给定整数值减 1）。
位于 ② 号转弯线的行索引与列索引相等。
位于 ③ 号转弯线的行索引等于列索引减 1。

"""

module = ""
case = "circle_number"

# number_list = [[0] * 4 for _ in range(4)]
# row, col, flag = 0, 0, 0
# for i in range(1, 17):
#     number_list[row][col] = i
#     if (row + col) == 3:
#         if row > col:
#             flag = 1
#         else:
#             flag = 2
#     if row == col and row > 0:
#         flag = 3
#     if row == col - 1 and col > 0:
#         flag = 4
#     if flag == 4:
#         row += 1
#     if flag == 3:
#         row -= 1
#     if flag == 2:
#         col -= 1
#     if flag == 1:
#         col += 1


SIZE = 4
array = [[0] * SIZE]
# 创建一个长度SIZE * SIZE的二维列表
for i in range(SIZE - 1):
    array += [[0] * SIZE]
# 该orient代表绕圈的方向
# 其中0代表向下，1代表向右，2代表向左，3代表向上
orient = 0
# 控制将1~SIZE * SIZE的数值填入二维列表中
# 其中j控制行索引，k控制列索引
j = 0
k = 0
for i in range(1, SIZE * SIZE + 1):
    array[j][k] = i
    # 如果位于图4.2中①号转弯线上
    if j + k == SIZE - 1:
        # j>k，位于左下角
        if j > k:
            orient = 1
        # 位于右上角
        else:
            orient = 2
    # 如果位于图5.2中②号转弯线上
    elif (k == j) and (k >= SIZE / 2):
        orient = 3
    # 如果j位于图5.2中③号转弯线上
    elif (j == k - 1) and (k <= SIZE / 2):
        orient = 0
    # 根据方向来控制行索引、列索引的改变
    # 如果方向为向下绕圈
    if orient == 0:
        j += 1
    # 如果方向为向右绕圈
    elif orient == 1:
        k += 1
    # 如果方向为向左绕圈
    elif orient == 2:
        k -= 1
    # 如果方向为向上绕圈
    elif orient == 3:
        j -= 1
# 采用遍历输出上面的二维列表
for i in range(SIZE):
    for j in range(SIZE):
        print '%02d ' % array[i][j],
    print("")
