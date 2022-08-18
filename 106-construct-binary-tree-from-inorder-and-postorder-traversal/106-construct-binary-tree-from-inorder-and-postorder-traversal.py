# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# lc sol
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        clarifications
            - assume inorder and postorder consist of unique values
            - assume each value of postorder also appears in inorder.
        
        Concept refresh
            - in-order: left-root-right
            - post-order: left-right-root
        
        '''
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None
            
            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]
 
            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root
        
        # neet way to build hashmap
        # enumerate() returns a tuple with the counter(index) and value
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        # print(idx_map)
       
        return helper(0, len(inorder) - 1)
        