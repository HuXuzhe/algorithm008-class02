'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-23 15:03:24
@LastEditors: hu_xz
@LastEditTime: 2020-06-23 15:33:23
'''
#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        for i in range(0, len(s), 2*k):
            res += s[i:i+k][::-1] + s[i+k:i+2*k]
        return res
    
# @lc code=end

#%%
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res, flag = "", True
        for i in range(0, len(s), k):
            res += s[i:i + k][::-1] if flag else s[i:i+k]
            flag = not flag
        return res 

# %%
