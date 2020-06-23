'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-23 14:27:20
@LastEditors: hu_xz
@LastEditTime: 2020-06-23 15:02:28
'''
#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 使用set提高代码执行效率
        # 用set代替字符串加速
        dicts = {c: s.count(c) for c in set(s)}
        for idx, char in enumerate(s):
            if dicts[char] == 1:
                return idx
        return -1        
# @lc code=end

#%%
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx
        return -1

# %%
