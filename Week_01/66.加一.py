#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(-1, -1-len(digits), -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + [0]* len(digits)
# @lc code=end

#%%
nums = [1,2,3]
for i in range(-1, -1-len(nums), -1):
    print(nums[i])    

# %%
nums = [1,2,3]
for i in range(-1, -4, -1):
    print(i)

nums[-3]
# %%
