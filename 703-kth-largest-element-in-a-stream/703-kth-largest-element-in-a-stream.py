# class KthLargest:
#     minHeap = []
#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         # add the nums in the min heap
#         for num in nums:
#             self.add(num)
        

#     def add(self, val: int) -> int:
#         # add new num in the min heap
#         heappush(self.minHeap, val)
        
#         # if heap has more than 'k' nums, remove one num
#         if len(self.minHeap) > self.k:
#             heappop(self.minHeap)
        
#         # return the Kth largest num
#         return self.minHeap[0]

# lc sol
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)