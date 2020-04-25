'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-04-22 23:31:13
@LastEditors: hu_xz
@LastEditTime: 2020-04-25 16:29:12
'''
#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
            
            
        

# @lc code=end

