class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #store freq of every val in hashmap
        #new hashmap with <key,array<Val>> to store all by freq
        #reverse the hashmap keys to access from back
        #keep pushing until count reached
        
        myMap = defaultdict(int)
        
        for num in nums:
            myMap[num] += 1
            
        matrix = [[] for i in range(len(nums)+1)]
        
        for number,value in myMap.items():
            matrix[value].append(number)
        
        res = []
        n = 0
        
        for row in range(len(matrix)-1,-1,-1):
            for num in range(len(matrix[row])):
                    res.append(matrix[row][num])
                    n += 1
                    if (n >= k):
                        return res
            
        
        
        
        
        
        

            