'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-05 00:00:48
@LastEditors: hu_xz
@LastEditTime: 2020-05-08 11:40:25
'''
#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            
        
# @lc code=end

