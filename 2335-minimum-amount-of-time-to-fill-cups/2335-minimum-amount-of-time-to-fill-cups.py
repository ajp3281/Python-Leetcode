class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        # simple max heap problem, take 2 at a time if you can

        heap = [-num for num in amount]
        heapq.heapify(heap)
        turns = 0
        while heap:
            if len(heap) > 1:

                first = heapq.heappop(heap)
                if first == 0:
                    return turns
                second = heapq.heappop(heap)

                if first < -1:
                    heapq.heappush(heap, first + 1)
                if second < -1:
                    heapq.heappush(heap, second + 1)

                turns += 1
            else:
                remaining = heapq.heappop(heap)
                turns += (-remaining)

        return turns

        