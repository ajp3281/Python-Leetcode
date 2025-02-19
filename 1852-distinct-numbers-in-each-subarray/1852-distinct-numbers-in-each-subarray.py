class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        # how to keep track 
        l = 0
        visited = defaultdict(int)
        res = []
        for r in range(len(nums)):
            visited[nums[r]] += 1

            if r - l + 1 == k:
                res.append(len(visited.keys()))
                visited[nums[l]] -= 1
                if visited[nums[l]] == 0:
                    visited.pop(nums[l])
                l += 1
            

        return res
        