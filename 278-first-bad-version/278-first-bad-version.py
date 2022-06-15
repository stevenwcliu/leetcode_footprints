# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # 大神模版
        # p, q = 0, n - 1 -> can't pass case: 1, 1
        p, q = 0, n
        while p < q:
            # mid = p + ( q - p ) / 2 -> 4.5
            mid = p + ( q - p ) // 2 # -> 4
            if isBadVersion(mid):
                q = mid
            else:
                p = mid + 1
        
        return p
        