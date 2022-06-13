class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # grok: Find the Missing Number
        i, n = 0, len(nums)
        while i < n:
            j = nums[i]
            if nums[i] < n and nums[i] != nums[j]: # check if the number at index i is less than the len(nums)??
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1

        # find the first number missing from its index, that will be our required number
        for i in range(n):
            if nums[i] != i:
                return i

        return n