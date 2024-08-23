class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def helper(index, partitions):
            if index >= len(s):
                res.append(partitions.copy())
                return 
            
            for i in range(index, len(s)):
                rest_of_string = s[index:i+1]
                if rest_of_string[:] == rest_of_string[::-1]:
                    partitions.append(rest_of_string)
                    helper(i+1, partitions)
                    partitions.pop()
            
        res = []
        helper(0, [])
        return res