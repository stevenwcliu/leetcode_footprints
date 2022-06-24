# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque([root])
        res = []
        level = 0
        
        while q:
            qLen = len(q)
            curLevel = []
            
            for _ in range(qLen):
                node = q.popleft()
                # curLevel.append(node)
                # curLevel.append(node.val) # wrong place
                if node:
                    curLevel.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                # wrong indentation
                '''
                if level % 2 == 0:
                    res.append(curLevel)
                else:
                    res.append(curLevel[::-1])
                level += 1
                '''
            # done with the current level    
            if level % 2 == 0:
                res.append(curLevel)
            else:
                res.append(curLevel[::-1])
            level += 1

        return res
                