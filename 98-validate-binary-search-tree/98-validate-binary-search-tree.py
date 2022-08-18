# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # bst 不能有相同value的node
        
        # concept refresh
        # BST: left < root and right > root
        
        def valid(node, left, right):
            if not node: # empty tree is a valid bst
                return True
            
            # wrong
            # if node.val < right or node.val > left:
            #     return False
            
            # ??
            if not(node.val < right and node.val > left): # nodes that breaks the BST
                return False
            
            return (valid(node.left, left, node.val) 
                    and valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))
                