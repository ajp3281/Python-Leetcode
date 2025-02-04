class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # three pointer?
        # keep one ptr at end of arr
        # left and mid to remove duplicates
        # whats the logic to remove duplicates?
        # left should be at first unique number
        # we need to swap back the numbers as well though
        # must be o(1) space as well

        # define a move function?

        # how to keep track of elems that need to be replaced?
        # will swapping while iterating cause an issue?

        # 0 0 1 1 1 2
        def swap(index):
            for r in range(index + 1, len(nums)):
                nums[r-1] = nums[r]

        swapped = 0
        for r in range(len(nums)-1, 1, -1):
            if nums[r] == nums[r-1] == nums[r-2]:
                swap(r)
                swapped += 1

        return len(nums) - swapped

        




        