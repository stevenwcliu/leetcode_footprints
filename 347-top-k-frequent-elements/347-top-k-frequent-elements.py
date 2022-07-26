class Solution:
	def topKFrequent(self, nums, k):
			# bucket sort: TC: O(n)
# 			cnt = {} # num of occu of each val
# 			freq = [[] for i in range(len(nums) + 1)] 
# 			# special arr 
# 			# -> index: cnt of an element
# 			# -> val: list vals that occur that particular times
			
# 			for n in nums: 
# 				cnt[n] = 1 + cnt.get(n, 0)
# 			for n, c in cnt.items():
# 			# d.items(): Returns a list of key-value pairs in a dictionary.
# 				freq[c].append(n) # val n occurs c times
			
# 			res = []
# 			# iterate freq in DECENDING order
# 			for i in range(len(freq) - 1, 0, -1):
# 			# len(freq) - 1: last index
# 				for n in freq[i]:
# 					res.append(n)
# 					if len(res) == k:
# 						return res
            
            # ref: grokking - Top 'K' Frequent Numbers (medium)
        
            # heap: TC: O(N + N * log K)
            
            # use hm the frequency of each number
            cnt = {}
            for num in nums:
                cnt[num] = cnt.get(num, 0) + 1
            
            minHeap = []
            
            for num, freq in cnt.items():
                heappush(minHeap, (freq, num))
                if len(minHeap) > k:
                    heappop(minHeap)
            
            res = []
            while minHeap:
                res.append(heappop(minHeap)[1])
            
            return res
                