class Solution:
    # 云神
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        p, q = 0, n - 1
        
        if n == 0:
            # wrong: return {-1, -1}
            return [-1, -1]
        
        while p < q:
            mid = p + (q - p) // 2
            if nums[mid] < target:
                p = mid + 1
            else:
                q = mid
        
        if nums[p] != target:
            return [-1, -1]
        p0 = p
        q = n - 1
        while p < q:
            mid = p + (q - p) // 2
            if nums[mid + 1] > target:
                q = mid
            else:
                p = mid + 1
        return [p0, p]