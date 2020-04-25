'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-04-25 16:59:10
@LastEditors: hu_xz
@LastEditTime: 2020-04-25 17:59:35
'''
#
# @lc app=leetcode.cn id=264 lang=python
#
# [264] 丑数 II
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp, a, b, c = [1]*n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]
        
# @lc code=end

