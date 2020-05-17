'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-11 15:16:02
@LastEditors: hu_xz
@LastEditTime: 2020-05-15 11:16:45
'''
#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = - n
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x*x, n / 2)
        

# @lc code=end

