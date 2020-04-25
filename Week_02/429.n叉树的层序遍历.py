'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-04-24 23:39:45
@LastEditors: hu_xz
@LastEditTime: 2020-04-25 18:12:51
'''
#
# @lc app=leetcode.cn id=429 lang=python
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
             return []
        previous_layer = [root]
        res = []
        while previous_layer:
            current_layer = []
            res.append([])
            for node in previous_layer:
                res[-1].append(node.val)
                current_layer.extend(node.children)
            previous_layer = current_layer
        return res

        
# @lc code=end

