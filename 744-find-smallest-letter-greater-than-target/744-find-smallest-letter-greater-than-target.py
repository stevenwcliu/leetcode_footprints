class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 仿大神
        n = len(letters)

        p, q = 0, n - 1
        while p < q:
            mid = p + (q - p) // 2
            if letters[mid] > target: # 看题意
                q = mid
            else: # target at right
                p = mid + 1
        # p == q
        # return letters[p % n]
        if target < letters[p]:
            return letters[p]
        else:
            return letters[0]