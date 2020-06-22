'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-03 22:55:37
@LastEditors: hu_xz
@LastEditTime: 2020-06-19 10:02:16
'''
#
# @lc app=leetcode.cn id=221 lang=python
#
# [221] 最大正方形
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        max_side = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0: 
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

                    if dp[i][j]:
                        max_side = max(max_side, dp[i][j])
        max_area = max_side ** 2
        return max_area
          
# @lc code=end

#%%
dp = [[0 for _ in range(5)] for _ in range(4)]
dp
# %%
