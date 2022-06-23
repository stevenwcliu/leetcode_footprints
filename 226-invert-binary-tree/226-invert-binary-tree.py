# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
#         if root is None: return
        
#         # post-order
#         left = self.invertTree(root.left)
#         right = self.invertTree(root.right)
#         root.left, root.right = right, left
        
#         return root
    
    # iterative
    # ref: LC sol

    def invertTree(self, root):
        if not root:
            return root

        q = collections.deque([root])

        while q:
            cur = q.popleft()
            cur.left, cur.right = cur.right, cur.left

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

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