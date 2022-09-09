class Solution:
    def permute(self, letters: List[int]) -> List[List[int]]:
        # ref: Algo Monster template
        # https://algo.monster/problems/permutations
        
        def dfs(self, path, used, res):
            if len(path) == len(letters):
                # res.append(path) # wrong -> append(path) actually appends a reference (memory address), we actually appended the same list
                res.append(path[:]) # deep copy -> creates a new list with elements being the same as current elements of path.
                # print("res:", res)
                return

            for i, letter in enumerate(letters):
                # skip used letters
                if used[i]:
                    continue
                # add letter to permutation, mark letter as used
                path.append(letter)
                # print("path: ", path)
                used[i] = True
                dfs(self, path, used, res)
                # remove letter from permutation, mark letter as unused
                path.pop()
                used[i] = False
        
        res = []
        dfs(self, [], [False] * len(letters), res)
        return res