class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        prefixes = [0] * (len(nums)+1)

        for query in queries:
            prefixes[query[0]] -= 1
            prefixes[query[1]+1] += 1

        print(prefixes)
        for i in range(1,len(prefixes)):
            prefixes[i] += prefixes[i-1]
        print(prefixes)

        for i in range(len(nums)):
            if nums[i] + prefixes[i] > 0:
                return False
        return True