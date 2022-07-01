class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # 103 w5 s1
        
        def rotate(c, n):
            return chr((ord(c) + n - ord('a')) % 26 + ord('a'))
        
        for i in range(len(shifts) - 1, -1, -1):
            shifts[i] += shifts[i + 1] if i < len(shifts) -1 else 0
        
        res = list(s)
        for i in range(len(res)):
            res[i] = rotate(res[i],shifts[i])
        return ''.join(res)
        