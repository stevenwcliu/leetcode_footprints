class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # grok: Bitonic Array Maximum
        # lc sol
        p, q = 0, len(arr) - 1
        while p < q:
            mid = p + (q - p) // 2
            if arr[mid] < arr[mid + 1]:
                p = mid + 1
            else:
                q = mid

        # at the end of the while loop, 'start == end'
        return p