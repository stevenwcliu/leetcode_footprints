# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # educative - Sum of Path Numbers
        def dfs(currentNode, track):
            if currentNode is None:
                return 0

            # calculate the path number of the current node
            track = 10 * track + currentNode.val

            # if the current node is a leaf, return the current path sum
            if currentNode.left is None and currentNode.right is None:
                return track

            # traverse the left and the right sub-tree
            return dfs(currentNode.left, track) + dfs(currentNode.right, track)
        
        return dfs(root, 0)

