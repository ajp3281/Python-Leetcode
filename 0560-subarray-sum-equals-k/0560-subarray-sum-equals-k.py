class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # prefix sum arr
        # 1 3 6
        # how do we know we can get left subarry?
        # hashmap to store counts
        hashmap = {}
        

        res = 0
        prefix = []
        # 1, 2, 1, 2, 1 target is 3
        # res should have 1,2 - 1,2 - 2,1 - 2,1
        # 1, 3, 4, 6, 7
        
        for i in range(len(nums)):
            if i >= 1:
                found_prefix = nums[i] + prefix[i-1]
            else:
                found_prefix = nums[i]
                
            # now need logic to calculate subarrays
            if found_prefix == k:
                res += 1
            if found_prefix - k in hashmap:
                res += hashmap[found_prefix - k]
                
            prefix.append(found_prefix)
            if found_prefix in hashmap:
                hashmap[found_prefix] += 1
            else:
                hashmap[found_prefix] = 1
                
        return res
        '''
            
        for i, num in enumerate(prefix):
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
                
        
        # iterate thru prefix array
        # at current index, either its equal to k or check if k-num in hashmap
        # how do we avoid double counting??
        print(hashmap)
        print(prefix)
        print(nums)
        
        # 1 1 1
        # 1 2 3
        # target is 2
        res = 0
        for num in nums:
            print(res, num)
            if num == k:
                res += 1
            if k - num in hashmap:
                res += 1
            print(res, num)
                
        return res
        '''
        