class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # lc sol with 大神namings
        p, q = 0, len(nums) - 1
        while p <= q:
            mid = p + (q - p) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[p]:
                if target >= nums[p] and target < nums[mid]:
                    q = mid - 1
                else:
                    p = mid + 1
            else:
                if target <= nums[q] and target > nums[mid]:
                    p = mid + 1
                else:
                    q = mid - 1
        return -1