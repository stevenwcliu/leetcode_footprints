class Solution:
    # from edu
    # TC: O(n)
    # SC: O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # low, high = 0, len(nums) - 1
        # i = 0
        # while i <= high:
        #     if nums[i] == 0:
        #         nums[i], nums[low] = nums[low], nums[i] # swap?
        #         i += 1
        #         low += 1
        #     elif nums[i] == 1:
        #         i += 1
        #     else: # arr[i] == 2
        #         nums[i], nums[high] = nums[high], nums[i]
        #         high -= 1
       
        # ref: fxmz
        zero = 0
        two = len(nums) - 1
        i = 0

        while i <= two:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1