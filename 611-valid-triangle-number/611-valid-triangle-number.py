class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # brute force: O(n^3) - Three nested loops to check every triplet
        # better: binary search?!
        '''
        clarification
        - sorted? no
        - input size? 1000 -> can't use n^3 approach, at most n^2
        - empty list or len(list) < 3 ? return 0
        - definition of a valid triangle? 
            - can they be all equal? yes
            - a + b > c -> valid ans
        - test case 1: [1, 1, 2] -> 1
        - test case 2: [1, 1, 1] -> 0, a + b > c
        - test case 3: [2, 2, 2, 3, 4] -> ?

        '''
        
        if len(nums) < 3:
            return 0
        
        nums.sort(reverse = True) # tc: nlogn, sc: nlogn  # **descending order
        
        N = len(nums)
        ans = 0 
        
        # a = b = c = 0 
        
        for c in range(N - 2): # O(n) # 枚举最长边
            a, b = N - 1, c + 1 # a 在数组的最右边， b: 第二长的边，在c后面那格数字
            while b < a: # O(c)
                if nums[a] + nums[b] > nums[c]: # 当前的最小边足够长了
                    ans += (a - b)
                    b += 1 # 第二长的边太长，可以 -1
                else:
                    a -= 1 # 当前的最小边太短
        
        return ans
                    
                    
            
        
        
        