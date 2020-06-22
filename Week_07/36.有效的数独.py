'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-15 14:48:03
@LastEditors: hu_xz
@LastEditTime: 2020-06-22 10:02:13
'''
#
# @lc app=leetcode.cn id=36 lang=python
#
# [36] 有效的数独
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        box = [[] for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    box_index = (i // 3)*3 + (j // 3)
                    if num not in rows[i] and num not in cols[j] and num not in box[box_index]:
                        rows[i].append(num)
                        cols[j].append(num)
                        box[box_index].append(num)
                    else:
                        return False
        return True
                                 
# @lc code=end

#%%
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        box = [[] for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                box_index = (i // 3) * 3 + j // 3
                if num != '.':
                    if num not in row[i] and num not in col[j] and num not in box[box_index]:
                        row[i].append(num)
                        col[j].append(num)
                        box[box_index].append(num)
                    else:
                        return False
        return True


#%%
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        raw = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        cell = [{} for _ in range(9)]
        
        for i in range(9):
            for j in range(9):                                 
                num = (3*(i//3) + j//3)#找单元
                temp = board[i][j]
                if temp != ".":
                    if temp not in raw[i] and temp not in col[j] and temp not in cell[num]:
                        raw [i][temp] = 1
                        col [j][temp] = 1
                        cell [num][temp] =1
                    else:
                        return False    
        return True