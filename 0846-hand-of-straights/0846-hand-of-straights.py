from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # initital thought is just sort
        
        # base case - check if len(hand) % groupsize == 0
        
        # greedy, look for next int at every time?
        # greedy - start at smallest int every time
        target = len(hand) // groupSize
        count = 0
        hashmap = Counter(hand)
        if len(hand) % groupSize != 0:
            return False
        
        heapq.heapify(hand)
        while hand:
            current_len = 0
            current_val = heapq.heappop(hand)
            if current_val in hashmap:
                while current_len < groupSize:
                    if current_val in hashmap:
                        hashmap[current_val] -= 1
                        if hashmap[current_val] == 0:
                            hashmap.pop(current_val)
                        current_val += 1
                        current_len += 1
                    else:
                        return False
                count += 1
                    
            if target == count:
                return True
        return False
            
            
        
        
        
            
            
        