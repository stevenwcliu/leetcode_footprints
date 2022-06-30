# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        
        # check if arr is an existed path in the given bt
        
        # return false as soon as we find a mismatch between the sequence and the node value.
        
        if not root:
            return False
        
        # educative - Path With Given Sequence
        def dfs(currentNode, arr, arrIndex):
            if currentNode is None:
                return False
            arrLen = len(arr)
            if arrIndex >= arrLen or currentNode.val != arr[arrIndex]:
                return False
            # if the current node is a leaf, add it is the end of the sequence, we have found a path
            if currentNode.left is None and currentNode.right is None and arrIndex == arrLen - 1:
                return True

              # recursively call to traverse the left and right sub-tree
              # return true if any of the two recursive call return true
            return dfs(currentNode.left, arr, arrIndex + 1) or dfs(currentNode.right, arr, arrIndex + 1)
            
        return dfs(root, arr, 0)
    
    