'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-06-11 18:03:28
@LastEditors: hu_xz
@LastEditTime: 2020-06-22 10:26:48
'''
#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # dfs
        if not board: return []
        rows, cols = len(board), len(board[0])
        def dfs(row, col):
            board[row][col] = '#'
            d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for dx, dy in d:
                next_row = row + dx
                next_col = col + dy
                if 1 <= next_row < rows and 1 <= next_col < cols and board[next_row][next_col] == 'O':
                    dfs(next_row, next_col)

        
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows-1 or j == cols-1) and board[i][j] == 'O':
                    dfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'

# @lc code=end

#%%
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # dfs
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or \
                board[i][j] == 'X' or board[i][j] == '#':
                return 

            board[i][j] = '#'  # 作标记   
            dfs(i-1, j)  # up
            dfs(i+1, j)  # down
            dfs(i, j-1)  # left
            dfs(i, j+1)  # right
            

        if not board: return 
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows-1 or j == cols-1) and board[i][j] == 'O':
                    dfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

#%%
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 递归dfs
        if not board: return 
        rows, cols = len(board), len(board[0])

        def dfs(i, j):
            board[i][j] = '#'
            d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for dx, dy in d:
                next_i = i + dx
                next_j = j + dy
                if 1 <= next_i < rows and 1 <= next_j < cols and board[next_i][next_j] == 'O':
                    dfs(next_i, next_j)
            
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows-1 or j == cols-1) and board[i][j] == 'O':
                    dfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

#%%
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # bfs
        import collections
        if not board: return 
        rows, cols = len(board), len(board[0])

        def bfs(i, j):
            deque = collections.deque()
            deque.append((i, j))
            d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            while deque:
                i, j = deque.popleft()
                if 0 <= i < rows and 0 <= j < cols and board[i][j] == 'O':
                    board[i][j] = '#'
                    for dx, dy in d:
                        deque.append((i+dx, j+dy))
               
                    
            
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows-1 or j == cols-1) and board[i][j] == 'O':
                    bfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'