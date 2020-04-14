#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            flag = 0
            for index in range(1, len(nums)):
                if nums[flag] != nums[index]:
                    flag += 1
                    nums[flag] = nums[index]
            return flag+1
        return 0
# @lc code=end

# 题解
"""
此处使用快慢指针，快指针用来遍历数组，与慢指针比较，若相同快指针+1；
否则，快指针的值放入慢指针索引+1的位置。
快指针遍历完数组，返回慢指针索引+1，即不重复项的长度。
时间复杂度O(n)
空间复杂度O(1)
"""
