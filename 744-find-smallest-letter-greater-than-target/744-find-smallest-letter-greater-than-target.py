class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 仿大神by yaoyao
        n = len(letters)

        p, q = 0, n - 1
        while p < q:
            mid = p + (q - p) // 2
            if letters[mid] > target: # 看题意 - 有时候要check mid + 1?
                q = mid
            else: # target at right
                p = mid + 1
        # p == q

        # if target < letters[p]:
        #     return letters[p]
        # else:
        #     return letters[0]
        return letters[p] if target < letters[p] else letters[0]