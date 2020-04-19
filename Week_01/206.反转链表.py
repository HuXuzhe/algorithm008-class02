'''
@Descripttion: 
@version: 3.X
@Author: hu_xz
@Date: 2020-04-18 20:37:22
@LastEditors: hu_xz
@LastEditTime: 2020-04-19 21:19:08
'''
#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
           cur.next, pre, cur = pre, cur, cur.next
        return pre
# @lc code=end

