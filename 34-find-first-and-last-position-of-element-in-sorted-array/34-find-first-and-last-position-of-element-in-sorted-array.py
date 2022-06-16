class Solution:
    # grok sol
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        res = [- 1, -1]
        res[0] = self.binary_search(nums, target, False)
        if res[0] != -1:  # no need to search, if 'key' is not present in the input array
            res[1] = self.binary_search(nums, target, True)
        return res


    # modified Binary Search
    def binary_search(self, arr, key, findMaxIndex):
        keyIndex = -1
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if key < arr[mid]:
                end = mid - 1
            elif key > arr[mid]:
                start = mid + 1
            else:  # key == arr[mid]
                keyIndex = mid
                if findMaxIndex:
                    start = mid + 1  # search ahead to find the last index of 'key'
                else:
                    end = mid - 1  # search behind to find the first index of 'key'
        return keyIndex