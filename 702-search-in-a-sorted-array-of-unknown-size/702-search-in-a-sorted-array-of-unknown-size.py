# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

# 云神
# TC: O(logn)
# SC: O(1)
class Solution:
    def search(self, reader, target):
        p, q = 0, 9999
        while p < q:
            mid = p + (q - p) // 2
            x = reader.get(mid + 1)
            if x == math.inf or x > target:
                q = mid
            else:
                p = mid + 1
        if reader.get(p) == target:
            return p
        else:
            return -1