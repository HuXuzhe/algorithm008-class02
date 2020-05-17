'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-13 00:31:29
@LastEditors: hu_xz
@LastEditTime: 2020-05-16 14:34:28
'''
#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
       
        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        
        def backtrack(sol, next_digits):
            if len(sol) == len(digits):
                res.append(sol)
                return 
            
            for num in phone[next_digits[0]]:
                backtrack(sol+num, next_digits[1:])


        res = []
        backtrack('', digits)
        return res

        
        
# @lc code=end
