class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        # 10-50, 60-120, 140,210
        # 0-15, 60-70
        # line sweep - add and subtract 1 to numbers?
        
        # 2 ptr approach, choose which window to increase?
        
        slots1.sort()
        slots2.sort()
        
        i = 0
        j = 0
        while i < len(slots1) and j < len(slots2):
            
            # how to decide to increase i or j
            # if slots2[1] < slots1[1] increase j 
            # elif slots1[1] < slots2[1] increase i
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
               
        return []
            #
            
        '''
        
        10-50 , 60 - 120 , 140-210
        0-15, 70-80
              
        
        
        
        linesweep = [0] * slots1[-1][1]
        
        for slot in slots1:
            
            for i in range(slot[0], slot[1]):
                linesweep[i] += 1
                
        
        for slot in slots2:
            for i in range(slot[0], slot[1]):
                linesweep[i] += 1
                
        left = 0
        right = 0
        
        while right < len(linesweep):
            while linesweep[right] == 2:
                if right - left == duration:
                    return [left + 1, right + 1] 
                right += 1

            left = right 
            right += 1
            
            
        return []
        '''
        
        