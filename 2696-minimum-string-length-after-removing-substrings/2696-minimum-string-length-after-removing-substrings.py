class Solution:
    def minLength(self, s: str) -> int:
        string_list = list(s)
        found = True
        while string_list and found:
            found = False
            for i in range(len(string_list)):
                if string_list[i] == 'D' and i > 0 and string_list[i-1] == 'C':
                    string_list.pop(i)
                    string_list.pop(i-1)
                    found = True
                    break
                    
                if string_list[i] == 'B' and i > 0 and string_list[i-1] == 'A':
                    string_list.pop(i)
                    string_list.pop(i-1) 
                    found = True
                    break
                    
        return len(string_list)
        