class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # tc O(s + t)
        # sc O(1)
        
        '''
        clarification:
        - is the length of s and t the same? YES
        - can I assume s and t only contains lowercase letters? YES
            -> ascii table: len(128)
            -> lowercase + uppercase: len(52)
        '''
        
        if len(s) != len(t):
            return -1
        
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] += 1
            cnt[ord(t[i]) - ord('a')] -= 1
        print(cnt)
        step = 0
        for val in cnt:
            if val > 0:
                step += val
        return step