class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        # should we just check all subarrays brute force?
        res = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if i == j:
                    res += arr[i]
                elif (j - i) % 2 == 0:
                    res += sum(arr[i:j+1])
                print(i,j)
                    
        return res
                
        