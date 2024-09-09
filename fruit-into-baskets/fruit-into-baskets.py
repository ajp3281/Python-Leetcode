class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window
        # keep window w max two fruits in it at once
        # 1,2,3,2,2,
        #   l     r 
        hashmap = {}
        left = 0
        res = 0
        for r in range(len(fruits)):
            if fruits[r] in hashmap:
                hashmap[fruits[r]] += 1
            else:
                hashmap[fruits[r]] = 1
            while len(hashmap) > 2:
                hashmap[fruits[left]] -= 1
                if hashmap[fruits[left]] == 0:
                    hashmap.pop(fruits[left])
                left += 1
                
            res = max(res, r - left + 1)
        return res
            
            
            