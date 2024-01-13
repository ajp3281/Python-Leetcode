class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        map1 = defaultdict(int)
        
        for num in nums:
            map1[num] += 1
            
        print(map1)
        
        i = 0
        for n in range(3):
            for j in range(map1[n]):
                nums[i] = n
                i += 1

                
        