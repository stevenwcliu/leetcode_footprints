from heapq import *
class MedianFinder:
    def __init__(self):
        self.l, self.r =[], []  # the smaller half of the list, max heap (invert min-heap)

    def addNum(self, num):

        if not self.l or num <= -1 * self.l[0]: # would l[0] work?
            heapq.heappush(self.l, -1 * num)
        else:
            heapq.heappush(self.r, num)

        # balance l/r
        if len(self.l) < len(self.r):
            heapq.heappush(self.l, -1 * self.r[0])
            heapq.heappop(self.r)
        elif len(self.l) - len(self.r) == 2:
            heapq.heappush(self.r, -1 * self.l[0])
            heapq.heappop(self.l)

    def findMedian(self):
        if len(self.l) > len(self.r):
            return -1 * self.l[0]
        else:
            return (-1 * self.l[0] + self.r[0]) / 2 

		


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()