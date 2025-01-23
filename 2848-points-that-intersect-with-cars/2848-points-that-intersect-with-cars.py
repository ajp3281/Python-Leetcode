class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:

        point_map = defaultdict(int)

        maxidx = 0
        for num in nums:
            point_map[num[0]] += 1
            point_map[num[1]+1] -= 1 
            maxidx = max(maxidx, num[0], num[1])
        
        points = sorted(point_map.keys())
        res = 0
        current_cars = 0
        for i in range(1,maxidx+1):
            if i in point_map:
                current_cars += point_map[i]
            if current_cars > 0:
                res += 1
        return res

