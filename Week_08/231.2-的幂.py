'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-16 15:15:53
@LastEditors: hu_xz
@LastEditTime: 2020-06-19 15:50:54
'''
#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 位运算 时间复杂度是O(1) 重要的是n & (n-1) == 0
        return n > 0 and n & (n-1) == 0
        

# @lc code=end

