class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        myMap = defaultdict(int)
        res = ""
        for char in chars:
            myMap[char] += 1
        
        print(myMap)
        
        
        for word in words:
            i = 0
            tempMap = myMap.copy()
            print(tempMap)
            while i < len(word):
                if word[i] not in tempMap or tempMap[word[i]] == 0:
                    break
                else:
                    tempMap[word[i]] -= 1
                    i += 1
            if i == len(word):
                res += word
                print(word)
            
            
                
        return len(res)
                    
            
                    
                    
            
                
        