class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # find the largest window with two unique numbers(check by len(hm))
        # -> shrink when len(hm) > 2
        n = len(fruits)
        start = 0 
        res = 0
        fruit_freq = {}
        
        for end in range(n):
            right = fruits[end]
            if right not in fruit_freq:
                fruit_freq[right] = 0
            fruit_freq[right] += 1
                
            while len(fruit_freq) > 2:
                left = fruits[start]
                fruit_freq[left] -= 1
                if fruit_freq[left] == 0:
                    del fruit_freq[left]
                start += 1
            
            res = max(res, end - start + 1)
        
        return res
        