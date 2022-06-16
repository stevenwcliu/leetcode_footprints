# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

# ref: https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/discuss/905437/Python-3-or-Trivial-Binary-Search-or-Explanation
class Solution:
    def search(self, reader, target):
        p, q = 0, 10000
        while p <= q:
            mid = (p + q) // 2
            val = reader.get(mid)
            if val == target: return mid
            elif val < target: p = mid+1
            else: q = mid-1 
        return -1