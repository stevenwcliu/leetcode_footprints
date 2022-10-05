class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # oct 5, 2022
        # nc
        hm = {} # val:index
        for i, num in enumerate(nums):
            # diff = num - target # mistake: diff is calculated by target minus num
            diff = target - num
            if diff in hm:
                return [hm[diff], i]
            hm[num] = i