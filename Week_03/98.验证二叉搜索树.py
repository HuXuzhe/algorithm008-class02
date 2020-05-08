'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-04 22:24:59
@LastEditors: hu_xz
@LastEditTime: 2020-05-08 11:39:22
'''
#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if node:
                val = node.val
                if val <= lower or val >= upper:
                    return False
                if not helper(node.left, lower, val):
                    return False
                if not helper(node.right, val, upper):
                    return False
            return True
        return helper(root)
        
# @lc code=end

