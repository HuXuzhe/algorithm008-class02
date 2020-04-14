#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = 0
        for index in range(0, len(nums)):
            if nums[index] != 0:
                nums[index], nums[flag] = nums[flag], nums[index]
                flag += 1
        return nums
# @lc code=end

