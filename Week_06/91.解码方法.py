'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-28 18:13:12
@LastEditors: hu_xz
@LastEditTime: 2020-06-18 15:37:45
'''
#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 第一种，两位数除了10、20以及大于26，有两种编码
        # 第二种，10以及20一种编码
        # 第三种，其他只有一种编码方式
        # 特例 0
        size = len(s)
        dp = [0] * (size+1)
        dp[0] = 1
        for i in range(1, size+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i > 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]
        return dp[-1]
            
           
# @lc code=end

#%%
def numDecodings(s):
        """
        :type s: str
        :rtype: int
        """
        # 第一种，两位数除了10、20以及大于26，有两种编码
        # 第二种，10以及20一种编码
        # 第三种，其他只有一种编码方式
        # 特例0
        size = len(s)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        if s[0] == '0':
            return 0
        dp[0] = 1

        for i in range(1, size):
            if s[i] != '0':
                dp[i] = dp[i - 1]

            num = 10 * (ord(s[i - 1]) - ord('0')) + (ord(s[i]) - ord('0'))

            if 10 <= num <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[size - 1]

