class Solution:
    def minSteps(self, s: str, t: str) -> int:
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
        