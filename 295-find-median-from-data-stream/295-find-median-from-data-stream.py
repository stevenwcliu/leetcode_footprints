from heapq import *
class MedianFinder:
    # amazon apr ng, indeed follow-up: 取最近k个

    def __init__(self):
        # small and large are member of this object so need to add self.
        # small: maxheap
        # large: minheap
        self.l, self.r = [], []
        

    def addNum(self, num: int) -> None:
        # implement maxheap in py: multiply each num by -1
        heapq.heappush(self.l, -1 * num)
        
        # make sure every num in small is <= every num in large
        # -1 * self.small[0] to get the true val
        if (self.l and self.r and
           (-1 * self.l[0] > self.r[0])):
            # some elements in small is greater than the smallest in large
            val = -1 * heapq.heappop(self.l)
            heapq.heappush(self.r, val)
        # uneven size
        if len(self.l) > len(self.r) + 1:
            val = -1 * heapq.heappop(self.l)
            heapq.heappush(self.r, val)
        if len(self.r) > len(self.l) + 1:
            val = heapq.heappop(self.r)
            heapq.heappush(self.l, -1 * val)
        

    def findMedian(self) -> float:
        # odd length
        if len(self.l) > len(self.r):
            return -1 * self.l[0]
        if len(self.r) > len(self.l):
            return self.r[0]
        # print("l: ", self.l)
        # print("r: ", self.r)
        
        return (-1 * self.l[0] + self.r[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()