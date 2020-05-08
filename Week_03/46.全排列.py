'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-07 17:47:03
@LastEditors: hu_xz
@LastEditTime: 2020-05-08 15:09:56
'''
#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
from itertools import permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(sol, nums, check):
            if len(sol) == n:
                res.append(sol)
                return 
            for i in range(n):
                if check[i] == 1:
                    continue
                
                # sol.append(nums[i])
                check[i] = 1
                backtrack(sol+[nums[i]], nums, check)
                # sol.pop()
                check[i] = 0
        
        n = len(nums)
        res = []
        check = [0 for _ in range(len(nums))]
        backtrack([], nums, check)
        return res
        
 
# @lc code=end

#%%
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        
        return [[v]+p for k,v in enumerate(nums) 
                for p in self.permute(nums[:k]+nums[k+1])]
