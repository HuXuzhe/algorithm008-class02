'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-14 17:04:56
@LastEditors: hu_xz
@LastEditTime: 2020-05-16 15:47:23
'''
#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
import heapq
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()

        gi, si = 0, 0
        count = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                si += 1
                gi += 1
                count += 1
            else:
                si += 1

        return count

     
# @lc code=end

