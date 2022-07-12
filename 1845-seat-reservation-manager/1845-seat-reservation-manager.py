# https://leetcode.com/problems/seat-reservation-manager/discuss/1186013/PythonPython3-solution-using-heap
class SeatManager:
    def __init__(self, n: int):
        self.lis = list(range(1,n+1))
        heapify(self.lis)
    def reserve(self) -> int:
        return heappop(self.lis)
    def unreserve(self, seatNumber: int) -> None:
        heappush(self.lis,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)