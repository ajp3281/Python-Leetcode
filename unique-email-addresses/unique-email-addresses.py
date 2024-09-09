class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # set to keep track of unique, 
        # iterate through emails - for . ignore and keep iterating for local
        # for + stop iterating through local and skip to domain start
        # always add domain start
        
        visited = set()
        for email in emails:
            local = ""
            domain = ""
            i = 0
            while i < len(email):
                if email[i] == "+":
                    # need to skip to domain name
                    while email[i] != "@":
                        i += 1
                    domain = email[i:]
                    i = len(email)
                else:
                    if email[i] != ".":
                        local += email[i]
                    i += 1
                if i < len(email) and email[i] == "@":
                    domain = email[i:]
                    i = len(email)
                
            visited.add(local + domain)
        print(visited)   
        return(len(visited))
                
                    
                
                    