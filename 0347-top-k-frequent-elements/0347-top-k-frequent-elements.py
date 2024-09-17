class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        arr = []
        for elem in counter.keys():
            arr.append((-counter[elem], elem))
        heapq.heapify(arr)
        res = []
        for i in range(k):
            res.append(heapq.heappop(arr)[1])
        return res
            

        
        
        