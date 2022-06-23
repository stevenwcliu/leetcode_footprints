# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # return the first bad version
        # tc 1: [0,0,0,1,1,1]
        # output: 3(?)
        
        # Clarifications:
        # at least 1 bad?
        # size of n?
        
        # return lower bound
        # p, q = 0, n - 1
        p, q = 1, n # according to constraint
        
        while p < q:
            mid = p + (q - p) // 2 
            if isBadVersion(mid): # search the left half
                q = mid
            else:
                p = mid + 1
        
        return p
                
        
        