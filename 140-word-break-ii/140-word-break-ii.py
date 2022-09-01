class Solution:
    # huahua
    # https://zxi.mytechroad.com/blog/leetcode/leetcode-140-word-break-ii/
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        mem = {}
        def wordBreak(s):
            if s in mem: return mem[s]
            ans = []
            if s in words: ans.append(s)
            for i in range(1, len(s)):
                right = s[i:]
                if right not in words: continue        
                ans += [w + " " + right for w in wordBreak(s[0:i])]
            mem[s] = ans
            return mem[s]
        return wordBreak(s)