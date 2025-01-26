class Solution:
    def largestInteger(self, num: int) -> int:

        # left to right
        # find largest even or odd number unless its equal to 8 or 9
        str_nums = str(num)
        nums = [int(char) for char in str_nums]
        replaced = 0
        even = False
        for i in range(len(nums)):
            current_num = nums[i]
            max_num = nums[i]
            even = True if current_num % 2 == 0 else False
            swapped_idx = 0
            for j in range(i,len(nums)):
                if even:
                    if nums[j] > max_num and nums[j] % 2 == 0:
                        swapped_idx = j
                        max_num = nums[j]
                if not even:
                    if nums[j] > max_num and nums[j] % 2 != 0:
                        swapped_idx = j
                        max_num = nums[j]

            if max_num > nums[i]:
                replaced += 1
                nums[i], nums[swapped_idx] = nums[swapped_idx], nums[i]

        res = [str(char) for char in nums]
        return int(''.join(res))
            
                
        