class Solution:
    def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1
    
#     def isHappy(self, n: int) -> bool:

#         seen = set()
#         while(n != 1):
#             cur = n
#             sum = 0
            
#             while cur != 0:
#                 sum += cur % 10 * cur % 10
#                 cur /= 10
            
#             if sum in seen:
#                 return False
#             seen.add(sum)
#             n = sum
        
#         return True
        
'''
// reference: https://www.youtube.com/watch?v=gW4hSbRoQoY&ab_channel=KevinNaughtonJr.

class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> seen = new HashSet<>();
        while(n != 1) {
            int current = n;
            int sum = 0;
            
            while(current != 0) {
                sum += (current % 10) * (current % 10);
                current /= 10;
            }
            
            if (seen.contains(sum)) {
                return false;
            }
            
            seen.add(sum);
            n = sum;
        }
        
        return true;
    }
}
'''