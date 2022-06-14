class Solution:
    def maxDistance(self, ps: List[int], m: int) -> int:
        ps.sort()
        n = len(ps)
        p = 1
        q = 1000000000
        
        while p < q:
            mid = p + (q - p) // 2
            cnt = 1
            prev = ps[0]
            for i in range(n):
                if prev + mid + 1 <= ps[i]:
                    cnt += 1
                    prev = ps[i]
            if cnt >= m:
                p = mid + 1
            else:
                q =mid
        
        return p
                