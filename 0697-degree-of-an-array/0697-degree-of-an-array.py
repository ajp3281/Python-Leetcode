class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # store freq in hashmap
        # go thru hash and find max val
        # cut array from left and right to find min length
        # what if theres two max
        
        # bucket sort instead ?
        
        
        myMap = defaultdict(int)
        
        for num in nums:
            myMap[num] += 1
          
        maxval = []
        maxcount = 0
        
        for number,count in myMap.items():
            if (count > maxcount):
                maxcount = count
                
        for number,count in myMap.items():
            if (count == maxcount):
                maxval.append(number)
                
        shortestlength = float(inf)
        
        for num in maxval:
            left = 0
            right = len(nums)-1
            while (nums[left] != num):
                left += 1
            while (nums[right] != num):
                right -= 1
            print(left)
            print(right)
            diff = right-left+1
            if diff < shortestlength:
                shortestlength = diff
        
        return shortestlength
            
            
            
            
            