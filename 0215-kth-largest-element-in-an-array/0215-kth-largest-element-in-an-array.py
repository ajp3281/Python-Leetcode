class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negativeNums = [-num for num in nums]
        heapq.heapify(negativeNums)
        print(negativeNums)
        for i in range(k-1):
            heapq.heappop(negativeNums)
            
        return -negativeNums[0]