#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        a = 1
        b = 2
        for _ in range(2, n):
            c = a + b
            a = b
            b = c
        return b
# @lc code=end

