class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # hm: lookup/insert/delete in O(1) average
        longest_streak = 0
        
        # line 9: the while loop would only execute if the current number is the beginning of a sequence
        # other wise it would skip that number
        for n in nums:
            if n - 1 not in num_set:  
                curr_num = n
                curr_streak = 1
                while curr_num + 1 in num_set:
                    curr_streak += 1
                    curr_num += 1
                longest_streak = max(longest_streak, curr_streak)
                
        return longest_streak
        