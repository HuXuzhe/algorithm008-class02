#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        k = 0
        for k in range(len(nums) - 2):
            if nums[k] > 0: break
            # skip the same k
            if k > 0 and nums[k] == nums[k-1]: continue
            i = k + 1
            j = len(nums) - 1 
            while i < j:
                if nums[i] + nums[j] > -nums[k]:
                    j -= 1
                elif nums[i] + nums[j] < -nums[k]:
                    i += 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    # skip the same elements
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res 
# @lc code=end

