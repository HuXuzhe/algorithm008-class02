#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#

# 三次反转法
# 时间复杂度O(n)
# 空间复杂度O(1)
# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 当k大于数组长度的时候，需要对k做除余处理
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        k %= len(nums)
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)
        return nums
# @lc code=end

#%%
#  pythonic
# 空间复杂度O(n)
# 时间复杂度O(n)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 当k大于数组长度的时候，需要对k做除余处理
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


