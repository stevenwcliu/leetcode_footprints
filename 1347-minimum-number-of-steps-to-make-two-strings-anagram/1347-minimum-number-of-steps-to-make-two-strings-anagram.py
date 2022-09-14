class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # tc O(s)
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
        
        cnt = [0] * 26 # sc O(26)
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] += 1
            cnt[ord(t[i]) - ord('a')] -= 1
        print(cnt)
        step = 0
        for val in cnt: # tc O(26)
            if val > 0:
                step += val
        return step
    
        '''
        cnt[i] positive means t is deficient of those characters and they need to be added to make it same
        cnt[i] is negative means t is in surplus of those characters and they need to be replaced.
        '''