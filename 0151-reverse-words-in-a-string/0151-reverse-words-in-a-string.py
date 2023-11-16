class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = []
        word = ""
        for character in s:
            if character == ' ' and len(word) >= 1:
                #print("check")
                words.append(word)
                word = ""
            elif character == ' ':
                continue
            else:
                #word = "".join([word,character])
                word += character
        words.append(word)
        
        result = []
        for i in range(len(words)-1,-1,-1):
            result.append(words[i])
            if i == 0:
                return "".join(result)
            result.append(' ')
            
        #print(result)
                
        