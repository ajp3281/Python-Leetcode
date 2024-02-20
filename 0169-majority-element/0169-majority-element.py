class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Map = defaultdict(int)
        current_max = 0
        res = None
        for num in nums:
            Map[num] += 1
            
        for index in Map:
            if Map[index] > current_max:
                res = index
                current_max = Map[index]
                
        return res
        