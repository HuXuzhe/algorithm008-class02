'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-23 15:35:22
@LastEditors: hu_xz
@LastEditTime: 2020-06-23 16:07:12
'''
#
# @lc app=leetcode.cn id=151 lang=python
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 去首尾的空格
        sub_s = s.strip()
        i = j = len(sub_s) - 1
        res = []
        while i >= 0:
            while i >= 0 and sub_s[i] != ' ': i -= 1
            res.append(sub_s[i+1: j+1])
            while sub_s[i] == ' ': i -= 1
            j = i
        return ' '.join(res)


# @lc code=end
#%%
# 库函数
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        s_list.reverse()
        return ' '.join(s_list)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        # s_list.reverse()
        return ' '.join(s_list[::-1])


# %%
