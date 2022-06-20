class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # ref: https://leetcode.com/problems/find-k-closest-elements/discuss/345730/Python3Find-k-closest-elements-Binary-Search/592440
        
		# edge cases
        if x <= arr[0]: 
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]

        p = 0
        q = len(arr) - k # max start point
        while p < q:
            mid = p + (q - p) // 2

            # mid + k is closer to x, discard mid by assigning left = mid + 1
            if x - arr[mid] > arr[mid + k] - x:
                p = mid + 1

            # mid is equal or closer to x than mid + k, remains mid as candidate
            else:
                q = mid

        # left == right, which makes both left and left + k have same diff with x
        return arr[p : p + k]