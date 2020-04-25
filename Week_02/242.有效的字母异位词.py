'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-04-21 23:26:54
@LastEditors: hu_xz
@LastEditTime: 2020-04-24 21:25:39
'''
#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)

            
        
        
# @lc code=end

