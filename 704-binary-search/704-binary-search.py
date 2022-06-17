class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 大神模版
        n = len(nums)
        p, q = 0, n - 1
        
        while p < q:
            mid = p + (q - p) // 2
            if nums[mid] >= target:
                q = mid
            else:
                p = mid + 1
        
        # p == q
        if nums[p] == target:
            return p
        else:
            return -1