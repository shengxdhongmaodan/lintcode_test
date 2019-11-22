#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author  : shengxd
@Contact : shengxd@huahuan.com
@File    :   fast_power.py
@Time    :   2019/11/14 15:12
@Desc    :

"""
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        # return pow(a,n) % b
        # 采用分治法
        if b == 1:
            return 0
        if a == 1 or n == 0:
            return 1
        if n == 1:
            return a % b
        # number = 0
        half_number = self.fastPower(a, b, n // 2)
        number = half_number * half_number * pow(a, n % 2) % b

        return number