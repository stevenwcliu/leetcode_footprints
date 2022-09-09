class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # ref: algo monster
        if len(digits) == 0: 
            return []
        
        KEYBOARD = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def dfs(self, path, res):
            if len(path) == len(digits):
                res.append(''.join(path)) # -> ["ad"]
                # res.append(path[:]) # doesn't work -> ["a", "d"]
                return

            next_number = digits[len(path)]
            for letter in KEYBOARD[next_number]:
                path.append(letter)
                dfs(self, path, res)
                path.pop()

        res = []
        dfs(self, [], res)
        return res