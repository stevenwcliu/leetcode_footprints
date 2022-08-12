class Solution:
    def romanToInt(self, s: str) -> int:
        # hm to match symbol to val
        # tc: O(n)
        # sc: O(1), hm of constant space
        
        # summary
        # largest to smallest: add them up
        # smaller before larger: subtract smaller
        
        roman = {"I": 1, "V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000 }
        
        res = 0
        
        for i in range(len(s)):
            # i + 1 < len(s) : check if i + 1 is still in-bound
            # roman[s[i]] < roman[s[i + 1]]: need to subtract roman[s[i]] from res
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        
        return res
        