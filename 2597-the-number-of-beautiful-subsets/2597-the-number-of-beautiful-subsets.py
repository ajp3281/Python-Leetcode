class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # backtracking solution
        # try to take an element if we dont have its complement already included
        # then remove and continue on

        # base case?
        # index is at end return 1
        # how to count results? every time we get into a new recursive call
        # we will be returning 1 so no need?
        # += recursive calls?
        # backtrack , try with and without
        # how should we keep track of visited?
        visited = set()
        def backtrack(i, visited):
            if i == len(nums)-1:
                if nums[i]-k not in visited and nums[i]+k not in visited:
                    return 1
                return 0

            visited.add(nums[i])
            take = 0
            if nums[i] - k not in visited and nums[i] + k not in visited:
                take = 1 + backtrack(i + 1, visited)
            visited.remove(nums[i])
            skip = backtrack(i+1, visited)
            

            return take + skip

        return backtrack(0, visited)
            
            