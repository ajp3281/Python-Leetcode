class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # [-1, -1, 1]
        '''
        gasneeded = [0] * len(gas)
        
        for i in range(len(gas)):
            gasneeded[i] = gas[i] - cost[i]
        
        if sum(gasneeded) < 0:
            return -1
        
        gasneeded *= 2
        # multiply gas needed by 2 - start from where gasneeded at currentpos > 0
        # if we cant continue, move up pointer
        left = 0
        right = 0
        while right < len(gasneeded):
            
            while gasneeded[left] < 0:
                left += 1
            else:
                right = left
                currentgas = gasneeded[right]
                while right - left < len(gas):
                    right += 1
                    if right >= len(gasneeded):
                        return -1
                    currentgas += gasneeded[right]
                    
                    if currentgas < 0:
                        break
                if right - left == len(gas):
                    return left
            left += 1
        return -1
        '''
        gasneeded = [0] * len(gas)
        
        for i in range(len(gas)):
            gasneeded[i] = gas[i] - cost[i]
        
        start = 0
        right = 0
        currentgas = 0
        totalgas = 0
        if sum(gasneeded) < 0:
            return -1
        while right < len(gasneeded):
            currentgas += gasneeded[right]
            totalgas += gasneeded[right]
            print(start, currentgas)
            if currentgas < 0 and start != len(gasneeded) - 1:
                currentgas = 0
                right += 1
                start = right
            else:
                right += 1
        if currentgas < 0:
            return -1
        else:
            return start
            
            
                    
        