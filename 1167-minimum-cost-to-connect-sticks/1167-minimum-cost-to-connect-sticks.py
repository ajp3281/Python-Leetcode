class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        heap = sticks.copy()
        heapq.heapify(heap)
        res = 0 
        while len(heap) > 1:
            left, right = heapq.heappop(heap), heapq.heappop(heap)
            res += left + right
            heapq.heappush(heap, left + right)

        return res

        