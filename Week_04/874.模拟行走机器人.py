'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-14 17:24:22
@LastEditors: hu_xz
@LastEditTime: 2020-05-16 21:09:59
'''
#
# @lc app=leetcode.cn id=874 lang=python
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        d = [(0,1), (1,0), (0,-1), (-1,0)]

        x, y = 0, 0
        res = tmp = 0
        ob = set(map(tuple, obstacles))

        for i in commands:
            if i == -1:
                tmp += 1
            elif i == -2:
                tmp -= 1

            else:
                for _ in range(i):
                    x += d[tmp%4][0]
                    y += d[tmp%4][1]

                    if (x, y) in ob:
                        x -= d[tmp%4][0]
                        y -= d[tmp%4][1]
            res = max(res, x**2 + y**2)
        return res
                    
# @lc code=end

