class Solution:
    def nextGreatestLetter(self, letters: List[str], key: str) -> str:
        # grok + 大神namings
        n = len(letters)

        p, q = 0, n - 1
        while p <= q:
            mid = p + (q - p) // 2
            if key < letters[mid]:
                q = mid - 1
            else: # key >= letters[mid]:
                p = mid + 1

        # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
        return letters[p % n]
