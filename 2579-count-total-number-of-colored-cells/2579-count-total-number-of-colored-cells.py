class Solution:
    def coloredCells(self, n: int) -> int:

        

        # check how many neighbors we add at every turn
        
        # 1 = 1, 2 = 5, 3 = 13, 4 = 25, 41
        cur = 1
        prev_added = 0
        running_sum = 1
        while cur < n:
            prev_added += 4
            running_sum += prev_added
            cur += 1

        return running_sum