#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author  : shengxd
@Contact : shengxd@huahuan.com
@File    :   print_num_by_recursion.py
@Time    :   2019/11/8 16:35
@Desc    :
用递归的方法找到从1到最大的N位整数。

用下面这种方式去递归其实很容易：

recursion(i) {
    if i > largest number:
        return
    results.add(i)
    recursion(i + 1)
}
但是这种方式会耗费很多的递归空间，导致堆栈溢出。你能够用其他的方式来递归使得递归的深度最多只有 N 层么？

您在真实的面试中是否遇到过这个题？
样例
样例 1:

输入 : N = 1
输出 :[1,2,3,4,5,6,7,8,9]
样例 2:

输入 : N = 2
输出 :[[1,2,3,4,5,6,7,8,9,10,11,12,...,99]
挑战
用递归完成，而非循环的方式。
"""
# import sys
import array
# sys.setrecursionlimit(9000000)  # 这里设置大一些

class Solution:
    """
    @param n: An integer
    @return: An array storing 1 to the largest number with n digits.
    """
    # def numbersByRecursion(self, n):
    #     # write your code here
    #     self.largest_num = int('9'*n)
    #     return self.get_numbers(self.largest_num)
    #
    # def get_numbers(self, num):
    #     # if num == 0:
    #     #     return
    #     # if 1 <= num < self.largest_num + 1:
    #     #     yield num
    #     # for r in self.get_numbers(num - 1):
    #     #     yield r
    #     # list()

    def numbersByRecursion(self, n):
        # write your code here
        self.largest_num = int('9' * n)
        self.int_array = array.array("i", [])
        self.get_numbers(1)
        return self.int_array

    def get_numbers(self, num):
        if self.largest_num < 10000:
            for i in range(num, self.largest_num):
                self.int_array.append(i)
            return
        else:
            if num > self.largest_num:
                return
            if 1 <= num <= self.largest_num:
                for i in range(num, num + 10000):
                    self.int_array.append(i)
                num = self.int_array[-1]
                if self.largest_num - num <= 10000:
                    for i in range(num+1, self.largest_num+1):
                        self.int_array.append(i)
                    return
                else:
                    self.get_numbers(num + 1)


if __name__ == "__main__":
    s = Solution()
    a = s.numbersByRecursion(5)
    print(a)
