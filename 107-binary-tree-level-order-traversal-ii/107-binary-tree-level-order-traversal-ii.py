# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # "BQ" - BFS with Queue
        
        q = deque([root])
        # q = collections.deque([root]) # alt.
        res = []
        
        while q:
            qLen = len(q)
            curLevel = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    curLevel.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(curLevel)
        
        # return res[:-1] # wrong
        return res[::-1]