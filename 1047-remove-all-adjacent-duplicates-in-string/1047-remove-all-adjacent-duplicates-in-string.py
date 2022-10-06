from collections import deque
class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = deque()
        for c in s:
            if output and c == output[-1]:
                output.pop()
            else:
                output.append(c)
        return ''.join(output)