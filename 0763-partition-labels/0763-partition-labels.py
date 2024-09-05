from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = Counter(s)
        print(hashmap)
        print(len(s))
        
        # visited set - make new partition when count of any added letters is 0
        
        res = []
        visited = set()
        count = 0
        for index, character in enumerate(s):
            visited.add(character)
            hashmap[character] -= 1
            count += 1
            if hashmap[character] == 0:
                # check if all characters are 0 and set counter 0 and keep going, else keep adding
                if all(hashmap[letter] == 0 for letter in visited):
                    visited.clear()
                    res.append(count)
                    count = 0
        return res
                
            
            