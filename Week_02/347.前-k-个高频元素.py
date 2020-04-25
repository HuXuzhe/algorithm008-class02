'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-04-25 18:16:53
@LastEditors: hu_xz
@LastEditTime: 2020-04-25 21:17:17
'''
#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        import heapq
        heapq_max = []
        c = {}
        res = []
        for item in nums:
            if item in c:
                c[item] += 1
            else:
                c[item] = 1

        for i in c:
            heapq.heappush(heapq_max,(-c[i], i))
        for _ in range(k):
            p = heapq.heappop(heapq_max)
            res.append(p[1])
        return res
            
        
        
# @lc code=end





