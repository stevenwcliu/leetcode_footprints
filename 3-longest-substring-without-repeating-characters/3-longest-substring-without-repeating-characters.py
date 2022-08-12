class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case check
        if s is None or len(s) == 0:
            return 0
        
        # sliding window
        # use set to maintain uniqueness in the cur window
        
        l, res = 0, 0
        char_set = set()
        
        for r in range(len(s)):
            c = s[r] # enter
            while c in char_set:
                # wrong: char_set.remove(c)
                char_set.remove(s[l]) # out
                l += 1
            char_set.add(c)
            res = max(res, r - l + 1) # calc
        return res