class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def helper(index, current, hashmap):
            if index >= len(nums):
                if tuple(current) not in hashmap:
                    res.append(current.copy())
                return
            
            if tuple(current) in hashmap:
                return
                           
            # how to handle duplicate subsets?
            
            # at every position you take or dont take
            # take last number of dupe?
            
            # naive approach - build all subsets and filter by using sets?
             
            #take
            print("before adding: ", current, index)
            current.append(nums[index])
            print("after adding: ", current, index)
            helper(index + 1, current, hashmap)
            
            hashmap.add(tuple(current))

            # skip
            print("before removal: ", current, index)
            current.pop()
            print("after removal: ", current, index)
            helper(index + 1, current, hashmap)

        
        res = []
        nums.sort()
        hashmap = set()
        helper(0, [], hashmap)
        return res
        