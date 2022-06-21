class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 云神
        res = [-1, -1]    
        n = len(nums)
        p, q = 0, n - 1
        
        # corner cases check
        if n == 0 or nums == None:
            return res
        
        while p < q:
            mid = p + (q - p) // 2
            if nums[mid] < target:
                p = mid + 1
            else:
                q = mid
        
        if nums[p] != target:
            return res
        
        # p0 = p
        res[0] = p
        q = n - 1
        
        while p < q:
            mid = p + (q - p) // 2
            if nums[mid + 1] > target:
                q = mid
            else:
                p = mid + 1
        
        if nums[p] == target:
            res[1] = p
        return res

        # yaoyao
        
        
    