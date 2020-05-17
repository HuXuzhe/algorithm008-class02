'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-14 16:28:30
@LastEditors: hu_xz
@LastEditTime: 2020-05-16 14:31:56
'''
#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                profit += tmp
        return profit
        
        
# @lc code=end

