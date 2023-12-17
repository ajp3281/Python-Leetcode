class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        count = 0
        for char in text:
            if char == ' ':
                count += 1
                
        if count == 0:
            return text
        
        words = text.split(' ')
        realwords = []
        for word in words:
            if len(word.strip()) != 0:
                realwords.append(word)
                
        if len(realwords) > 1:
            spaces = count//(len(realwords)-1)
        else:
            spaces = 0
            
        if len(realwords) > 1:
            leftover_spaces = count % (len(realwords)-1)
        else:
            leftover_spaces = count
        
        result = ""
        for i in range(len(realwords)-1):
            result += realwords[i]
            for i in range(spaces):
                result += " "
                
        result += realwords[len(realwords)-1]
        
        for i in range(leftover_spaces):
            result += " "
            
        return result
            
        