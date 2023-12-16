class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        map1 = defaultdict(list)
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    map1[1].append((i,j))
                    
        map2 = defaultdict(list)
        for i in range(len(img2)):
            for j in range(len(img2[0])):
                if img2[i][j] == 1:
                    map2[1].append((i,j))
                    
        resultMap = defaultdict(int)
        maxCount = 0
        
        for row1,col1 in map1[1]:
            for row2,col2 in map2[1]:
                distance = (row2-row1,col2-col1)
                resultMap[distance] += 1
        
        for _,overlap in resultMap.items():
            if (overlap > maxCount):
                maxCount = overlap
        
        return maxCount