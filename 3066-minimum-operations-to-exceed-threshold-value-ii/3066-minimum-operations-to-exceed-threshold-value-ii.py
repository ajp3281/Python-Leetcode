class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        # heap problem?
        # we need to keep it sorted to take 2 min elems every time
        # min heap - only add to heap if num < k
        '''
        heap = []
        for num in nums:
            if num < k:
                heap.append(num)
        '''
        heap = nums.copy()

        heapq.heapify(heap)
        ops = 0
        while heap:
            if heap[0] >= k:
                return ops
            first, second = heapq.heappop(heap), heapq.heappop(heap)
            res = (min(first, second) * 2) + max(first, second)
            heapq.heappush(heap, res)
            ops += 1

        return ops

        