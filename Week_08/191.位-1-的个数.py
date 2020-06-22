'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-16 14:49:27
@LastEditors: hu_xz
@LastEditTime: 2020-06-22 10:19:41
'''
#
# @lc app=leetcode.cn id=191 lang=python
#
# [191] 位1的个数
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 位运算
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
            
  
# @lc code=end
#%%
# 将十进制转换成二进制，再统计1的个数
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 每次对2取余判断是否是1，是的话就conut+1
        count = 0
        while n:
            if n % 2:
                count += 1
            n //= 2
        return count