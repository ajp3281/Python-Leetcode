class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        # prefix problem
        prefix_one = [grid[0][0]]
        prefix_two = [grid[1][0]]

        for i in range(1,len(grid[0])):
            prefix_one.append(prefix_one[i-1] + grid[0][i])
            prefix_two.append(prefix_two[i-1] + grid[1][i])

        # robot will either get rest of top row
        # or to the left of bottom row based on crossing point
        res = float("-inf")
        for i in range(len(grid[0])):
            rest_of_right = prefix_one[-1] - prefix_one[i]
            rest_of_left = prefix_two[i]

            print(rest_of_left,rest_of_right)
            res = max(res, min(rest_of_right, rest_of_left))

        return res

            

        