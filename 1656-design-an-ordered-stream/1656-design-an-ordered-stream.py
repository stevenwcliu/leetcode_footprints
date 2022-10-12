class OrderedStream:
    # ref: https://leetcode.cn/problems/design-an-ordered-stream/solution/pythonjavatypescriptgo-by-himymben-ne0f/


    def __init__(self, n: int):
        self.data = [""] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey] = value
        ans = []
        while self.ptr < len(self.data) and self.data[self.ptr]:
            ans.append(self.data[self.ptr])
            self.ptr += 1
        return ans
