class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # only start from unique vals
        def backtrack(i,path):
            if i >= len(nums):
                subsets.append(path.copy())
                return

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            # skip path will not include any dupes!
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, path)

        subsets = []
        backtrack(0, [])
        return subsets
        