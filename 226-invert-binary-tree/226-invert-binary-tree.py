# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None: return
        
        # post-order
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        
        return root
        
#         def helper (self, root, res):
#             if root is None: return
#             self.helper(root.left, res)
#             self.helper(root.right, res)
#             res.append(root.val)

#         def postorderTraversal(self, root):
#             res = []
#             self.helper(root, res)
#             return res