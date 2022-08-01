class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            # base case
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            # i could still be out of bound

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            # i < len(s): check if i is in-bound
            if (j + 1) < len(p) and p[j + 1] == '*':
                # two choices when we encounter *
                cache[(i, j)] = (dfs(i, j + 2) or # don't use *
                (match and dfs(i + 1, j))) # use *, only can use * when first char are matched
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return cache[(i, j)]

        return dfs(0,0)
        