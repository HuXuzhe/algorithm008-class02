'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-28 17:17:30
@LastEditors: hu_xz
@LastEditTime: 2020-06-18 14:57:23
'''
#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 复杂度O(m*n)
        # if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0: continue
                elif i == 0: grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0: grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]

# @lc code=end

