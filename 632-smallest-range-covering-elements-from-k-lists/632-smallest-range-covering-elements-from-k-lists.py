# cp 103
# p.55 @https://docs.google.com/presentation/d/1eFoYn0yIoA64xVIBiS_-H5XlEkWKo-1kK8IDURV33NI/edit#slide=id.g1342bd8af9d_0_17

class Solution:
    def smallestRange(self, data: List[List[int]]) -> List[int]:
        if len(data) == 0:
            return []

        # start our heap with the first element from every single list
        heap = []
        for list_index in range(len(data)):
            heap.append((data[list_index][0], list_index, 0))

        heapq.heapify(heap)

        # Set the current min/max bounds that will be our answer
        ans = (-sys.maxsize - 1), sys.maxsize
        right = max(item[0] for item in heap)

        while heap:
            left, list_index, j = heapq.heappop(heap)

            # The new minimum presents a larger lowerbound => smaller range
            if right - left < ans[1] - ans[0]:
                ans = left, right

            # If we've run out of data in a list, then we can exit.
            # This is because we've created the smallest range that includes the last value from this list,
            # hence any future ranges found will be larger.
            if j + 1 == len(data[list_index]):
                return ans

            # The value we pulled from the MIN heap was from the i'th list,
            # so we will replace it from the same list
            next_num = data[list_index][j+1]

            # Set the new upper-range and add the new element to the min heap.
            right = max(right, next_num)
            heapq.heappush(heap, (next_num, list_index, j + 1))

        return [ans[0], ans[1]]
