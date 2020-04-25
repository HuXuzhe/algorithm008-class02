'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-04-23 20:50:52
@LastEditors: hu_xz
@LastEditTime: 2020-04-25 16:26:47
'''
#
# @lc app=leetcode.cn id=589 lang=python
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        stack, res = [root,], []
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            stack.extend(tmp.children[::-1])
        return res
            

# @lc code=end

