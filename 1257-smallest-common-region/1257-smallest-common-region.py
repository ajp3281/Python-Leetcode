class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        # quebec -> Canada -> North America -> Earth
        # New York > United States -> North America
        
        # return NA
        hashmap = {}
        for region in regions:
            for son in region[1:]:
                hashmap[son] = region[0]
            
        print(hashmap)
        path = set()
        path.add(region1)
        current = region1
        while current in hashmap:
            current = hashmap[current]
            path.add(current)
        
        current = region2
        while current not in path:
            current = hashmap[current]
            
        return current
            
        
            
        
        
        