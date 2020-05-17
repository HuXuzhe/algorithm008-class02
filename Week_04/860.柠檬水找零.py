'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-14 16:01:30
@LastEditors: hu_xz
@LastEditTime: 2020-05-16 14:27:29
'''
#
# @lc app=leetcode.cn id=860 lang=python
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five, ten = 0, 0
        for bill in bills:
            if bill == 5: five += 1
            elif bill == 10: ten, five = ten + 1, five - 1
            elif ten > 0: ten, five = ten - 1, five - 1
            else: five -= 3
            if five < 0: return False
        return True
        

# @lc code=end

