'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-05-06 10:53:06
@LastEditors: hu_xz
@LastEditTime: 2020-05-08 11:46:52
'''
#
# @lc app=leetcode.cn id=297 lang=python
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def doit(node):
            if node:
                res.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                res.append('#')

        res = []
        doit(root)
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def doit():
            val = next(vals)
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = doit()
            root.right = doit()
            return root
        vals = iter(data.split())
        return doit()
        
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

