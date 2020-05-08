'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-08 15:12:42
@LastEditors: hu_xz
@LastEditTime: 2020-05-08 15:47:02
'''
#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(sol, nums, check):
            if len(sol) == n:
                res.append(sol)
                return 
            
            for i in range(n):
                # 用过的元素不能再使用
                if check[i] == 1:
                    continue
                # 当前元素和前一个元素相同，前一个元素而且没有被使用过
                if i > 0 and nums[i-1] == nums[i] and check[i-1] == 0:
                    continue
                check[i] = 1
                backtrack(sol+[nums[i]], nums, check)
                check[i] = 0
            

        n = len(nums)
        res = []
        check = [0 for _ in range(n)]
        nums.sort()
        backtrack([], nums, check)
        return res
# @lc code=end

