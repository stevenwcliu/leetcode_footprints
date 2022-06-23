class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # find left bound
        
        p, q = 0, len(nums)
        
        while p < q:
            mid = (p + q) // 2
            # print(nums[mid])
            if nums[mid] < target:
                p = mid + 1
            else:
                q = mid
        
        return p
    
        