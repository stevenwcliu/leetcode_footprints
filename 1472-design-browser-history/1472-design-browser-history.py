class BrowserHistory:
    '''
    需要有个数据结构能够很快的前进和后退 n 步，第一感觉是栈，
    但是一般认为栈中的数据弹出之后就不存在了，因此后退了之后就不能前进。
    故最终使用数组来模拟。

    使用一个数组his保存所有的访问记录，使用cur保存当前处于数组中的哪个位置。

    __init__(str)函数：初始化时把homepage放入数组中。
    forward(steps)函数：会让cur前进steps步，但是注意不能超出数组的右边界。
    back(steps)函数：会让cur后退steps步，但是注意不能少于数组的左边界。
    visit(url)函数：会先把cur位置以后的所有历史记录清空，然后把url放到his数组的后面。

    '''

    def __init__(self, homepage: str):
        self.his = [homepage]
        self.cur = 0


    def visit(self, url: str) -> None:
        while self.his and len(self.his) - 1 > self.cur:
            self.his.pop()
        self.his.append(url)
        self.cur += 1


    def back(self, steps: int) -> str:
        self.cur -= min(self.cur, steps)
        return self.his[self.cur]
        

    def forward(self, steps: int) -> str:
        self.cur += steps
        self.cur = min(self.cur, len(self.his) - 1)
        return self.his[self.cur]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)