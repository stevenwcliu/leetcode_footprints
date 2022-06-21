# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        '''
        - delete the node by "replacing" the node with node.next
          -> node.val change to node.next.val
          -> node.next change to node.next.next        
        '''
        # ref: https://leetcode.com/problems/delete-node-in-a-linked-list/discuss/354949/Python3-change-value-and-change-pointer
        node.val = node.next.val
        node.next = node.next.next
        