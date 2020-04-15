#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, res = 0, len(height)-1, 0
        while l < r:
            if height[l] < height[r]:
                res = max((r-l) * min(height[l], height[r]), res)
                print('res1', res)
                l += 1
            else:
                res = max((r-l) * min(height[l], height[r]), res)
                print('res2', res)
                r -= 1
        return res
# @lc code=end
#%%
class Solution:
    def maxArea(self, height):
        l, r, res = 0, len(height)-1, 0
        while l < r:
            if height[l] < height[r]:
                res = max((r-l) * min(height[l], height[r]), res)
                print('res1', res)
                l += 1
            else:
                res = max((r-l) * min(height[l], height[r]), res)
                print('res2', res)
                r -= 1
        return res
s = Solution()

height =  [2,3,4,5,18,17,6]
res = s.maxArea(height)
res 

# %%
