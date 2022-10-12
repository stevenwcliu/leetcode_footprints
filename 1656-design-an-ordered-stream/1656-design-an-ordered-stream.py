class OrderedStream:
    # ref: https://leetcode.cn/problems/design-an-ordered-stream/solution/pythonjavatypescriptgo-by-himymben-ne0f/


    def __init__(self, n: int):
        # self.data = [""] * (n + 1) # list 只能从0 - n; 但ptr 有可能到 n + 1
        self.data = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey] = value
        ans = []
        # while self.ptr < len(self.data) and self.data[self.ptr]:
        while self.ptr in self.data:
            ans.append(self.data[self.ptr])
            self.ptr += 1
        return ans
