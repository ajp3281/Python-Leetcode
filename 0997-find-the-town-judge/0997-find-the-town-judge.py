class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustset = defaultdict(list)
        trustedset = defaultdict(list)
        for i in range(len(trust)):
            #if trust[i][1] not in trustedset:
            trustedset[trust[i][1]].append(trust[i][0])
            trustset[trust[i][0]].append(trust[i][1])
                
        print(trustedset)
        print(trustset)
                
        
        for i in range(1,n+1):
            if i not in trustset:
                if len(trustedset[i]) == n-1:
                    return i 
                
        return -1
        
        
        
        
            
        