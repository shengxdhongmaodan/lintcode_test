#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author  : shengxd
@Contact : shengxd@huahuan.com
@File    :   narcissistic_number.py
@Time    :   2019/11/4 19:06
@Desc    :
Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits. See wiki

For example the 3-digit decimal number 153 is a narcissistic number because 153 = 13 + 53 + 33.

And the 4-digit decimal number 1634 is a narcissistic number because 1634 = 14 + 64 + 34 + 44.

"""
import os

module = ""
case = "narcissistic_number"



def get_narcissistic_number(n):
    result_list = []
    if n == 1:
        for j in range(10):
            if j == pow(j,n):
                result_list.append(j)
    if n == 2:
        for i in range(1,10):
            for j in range(10):
                value = i*10 + j
                match_value = pow(i,n) + pow(j,n)
                if value == match_value:
                    result_list.append(value)
    if n == 3:
        for k in range(1,10):
            for i in range(10):
                for j in range(10):
                    value = k*100 + i * 10 + j
                    match_value = pow(k, n) + pow(i, n) + pow(j, n)
                    if value == match_value:
                        result_list.append(value)
    if len(result_list) == 0:
        print("%d 位数 has none narcissistic_number" % n)
    else:
        return result_list


if __name__ == "__main__":
    print(get_narcissistic_number(3))
