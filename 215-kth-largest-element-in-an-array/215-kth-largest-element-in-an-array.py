from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        
        for i in range(k):
            heappush(minHeap, nums[i])
        print("heap: ", minHeap)
            
        for i in range(k, len(nums)):
            # if nums[i] > minHeap(0): # replaced the smallest num in heap
            if nums[i] > minHeap[0]:
                heappop(minHeap)
                heappush(minHeap, nums[i])
        
        return minHeap[0] # the heap has the bottom 'k' nums