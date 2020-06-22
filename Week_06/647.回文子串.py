'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-05 10:31:03
@LastEditors: hu_xz
@LastEditTime: 2020-06-19 10:40:56
'''
#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = True
        
        for j in range(1, size):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
        count = 0
        for i in range(size):
            for j in range(i, size):
                if dp[i][j] == True:
                    count += 1 
        return count
# @lc code=end

#%%

# %%
