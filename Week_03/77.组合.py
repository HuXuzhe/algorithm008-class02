'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-07 11:42:48
@LastEditors: hu_xz
@LastEditTime: 2020-05-08 12:31:22
'''
#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#
# @lc code=start
from itertools import combinations
import copy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n <=0 or k <= 0 or k > n:
            return []
        def treeback(first=1, pre=[]):
            if len(pre) == k:
                res.append(pre[:])
                return 
            for i in range(first, n-(k-len(pre))+2):
                pre.append(i)
                treeback(i+1, pre)
                pre.pop()
                
        res = []
        treeback()
        return res
# @lc code=end

#%%
from itertools import combinations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(combinations(range(1, n+1), k))

# %%
