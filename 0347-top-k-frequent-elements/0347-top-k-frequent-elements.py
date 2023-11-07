class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #store freq of every val in hashmap
        #new hashmap with <key,array<Val>> to store all by freq
        #reverse the hashmap keys to access from back
        #keep pushing until count reached
        
        myMap = defaultdict(int)
        for num in nums:
            myMap[num] += 1
        
        bucketarray = [[] for _ in range(len(nums)+1)]
        
        for key,val in myMap.items():
            bucketarray[val].append(key)
            
        res = []
        n = 0
        for row in range(len(bucketarray)-1,-1,-1):
            for num in bucketarray[row]:
                res.append(num)
                n += 1
                if (n >= k):
                    return res
        
        

            