# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # ref: https://leetcode.com/problems/path-sum-ii/discuss/1151494/Python-O(n)-by-DFS-w-Comment
#         def dfs( node, cur_path, target ):
            
#             ## base case aka stop condition
#             if not node:
                
#                 # empty node or empty tree
#                 return
            
#             ## general cases
            
#             # update target level
#             target = target-node.val
        
#             if (not node.left) and (not node.right) and target == 0:
                
#                 # check on leaf node
#                 cur_path.append( node.val )
#                 answer.append( cur_path )
#                 return
            
#             # Solve subproblem in DFS
#             dfs( node.left, cur_path + [node.val], target )
#             dfs( node.right, cur_path + [node.val], target )
            
#             return
#         # --------------------------------------
        
#         answer = []
        
#         dfs(node=root, cur_path=[], target=targetSum)
        
#         return answer

    def pathSum(self, root, required_sum):
        # educative

        def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
            if currentNode is None:
                return

        # add the current node to the path
            currentPath.append(currentNode.val)

        # if the current node is a leaf and its value is equal to required_sum, save the current path
            if currentNode.val == required_sum and currentNode.left is None and currentNode.right is None:
                allPaths.append(list(currentPath))
            else:
            # traverse the left sub-tree
                find_paths_recursive(currentNode.left, required_sum - currentNode.val, currentPath, allPaths)
            # traverse the right sub-tree
                find_paths_recursive(currentNode.right, required_sum - currentNode.val, currentPath, allPaths)

            # remove the current node from the path to backtrack,
            # we need to remove the current node while we are going up the recursive call stack.
            del currentPath[-1]
        
        allPaths = []
        find_paths_recursive(root, required_sum, [], allPaths)
        return allPaths