class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 大神模版
        n = len(nums)
        # p, q = 0, n -> wrong
        p, q = 0, n - 1
        # while p < q: -> wrong
        while p <= q:
            # mid = p + ( q - p ) / 2 -> 4.5
            mid = p + ( q - p ) // 2 # -> 4
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                q = mid - 1
            else:
                p = mid + 1
        
        return -1
        