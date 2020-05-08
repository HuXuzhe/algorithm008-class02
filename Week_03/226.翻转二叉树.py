'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-03 10:26:42
@LastEditors: hu_xz
@LastEditTime: 2020-05-07 10:59:35
'''
#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 时间复杂度是O(n)
        if not root: 
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# @lc code=end

