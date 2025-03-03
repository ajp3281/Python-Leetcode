class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        # seems like a classic 2 ptr problem
        # find pivot and work outwards?
        # wait why not just rebuild from scratch? 
        # keep track of all elements less than equal to and greater than then combine

        less = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            if num == pivot:
                equal.append(num)
            if num > pivot:
                greater.append(num)

        return less + equal + greater

        