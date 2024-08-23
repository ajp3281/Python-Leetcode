class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def helper(index, partition):
            if index == len(s):
                res.append(partition.copy())
                return
                
            for i in range(index, len(s)):
                # take a segment
                segment = s[index:i+1]
                if segment == segment[::-1]:
                    partition.append(segment)
                    helper(i+1, partition)
                    partition.pop()
                
        
        res = []
        helper(0, [])
        return res