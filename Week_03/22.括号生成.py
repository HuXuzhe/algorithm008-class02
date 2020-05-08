'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-04-29 10:44:59
@LastEditors: hu_xz
@LastEditTime: 2020-05-06 10:10:34
'''
#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(cur, l_num, r_num):
            if l_num == 0 and r_num == 0:
                res.append(cur)
                return 
            if l_num > 0:
                dfs(cur+'(', l_num-1, r_num)
            if r_num > 0 and r_num > l_num:
                dfs(cur+')', l_num, r_num-1)

        res = []
        dfs('', n, n)
        return res
        # @lc code=end

