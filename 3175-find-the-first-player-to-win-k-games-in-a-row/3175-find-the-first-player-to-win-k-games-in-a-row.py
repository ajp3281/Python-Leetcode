class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        
        # deque to store skills
        # if first player wins, increase count. if count == k return player
        # if first player loses, set count to 0. 
        
        q = deque([])
        if k > len(skills):
            return skills.index(max(skills))
        
        for i in range(len(skills)):
            q.append(i)
        print(q)
        
        count = 0
        while q:
            
            p1 = q.popleft()
            p2 = q[0]
            if skills[p1] > skills[p2]:
                q[0] = p1
                q.append(p2)
                count += 1
                if count == k:
                    return p1
            else:
                count = 1
                if count == k:
                    return p2
                q.append(p1)
        return -1
            
                
        