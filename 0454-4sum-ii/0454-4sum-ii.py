class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        count = 0
        map1 = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                map1[num1+num2] += 1
        
        for num3 in nums3:
            for num4 in nums4:
                if -(num3+num4) in map1:
                    count += map1[-(num3+num4)]
                    
        return count
        