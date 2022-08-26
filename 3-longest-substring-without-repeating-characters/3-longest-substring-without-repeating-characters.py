class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        clarification
        - s is Null or len(s) -> return 0
        - case: s = "aaaa" -> output: 1
        - case: s = "abccba" -> output: 3
        
        plan
        - sliding window: tc O(n)
        - use hash set to make sure of uniqueness of char in the current window: sc O(1), worst case O(n)? if all char in s are distinct
        - return the len of the largest window
        
        evaluation
        - tc : O(n), iterate the given s once
        - sc: O(n), space for the char_set, worst case all chars are disctinct
        '''
        
        # case: s = "aaaa" -> output: 1
        #               l 
        #               r
        # char_set = {a}
        # res = 1
                     
        if s is None or len(s) == 0:
            return 0
        
        l = res = 0
        char_set = set()
        
        for r in range(len(s)):
            char = s[r]
            while char in char_set: # duplicates found
                char_set.remove(s[l]) # remove the leftmost of the cur windwo
                l += 1
            char_set.add(char)
            res = max(res, r - l + 1)
        
        return res
        