class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.original = list(nums)
        

    def reset(self) -> List[int]:
        return self.original
        

    def shuffle(self) -> List[int]:
        nlen = len(self.arr)
        for i in range(nlen):
            j = random.randint(0,i)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr
        
        
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()