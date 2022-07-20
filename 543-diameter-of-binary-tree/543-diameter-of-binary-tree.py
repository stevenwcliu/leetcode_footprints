# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Jul 20
        # 所谓二叉树的直径，就是左右子树的最大深度之和，那么直接的想法是对每个节点计算左右子树的最大高度，得出每个节点的直径，从而得出最大的那个直径。
        def longest_path(node):
            if not node:
                return 0
            nonlocal diameter
            # recursively find the longest path in
            # both left child and right child
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)
            
            # 后序遍历位置顺便计算最大直径
            # update the diameter if left_path plus right_path is larger
            diameter = max(diameter, left_path + right_path)

            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1

        diameter = 0
        longest_path(root)
        return diameter
        