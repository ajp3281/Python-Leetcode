class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        
        # given k replacements with k indices and k courses. 
        # if source[index] occurs in s[index], replace it with target[index]
        # else do nothing
        # indexes on replacements will not overlap
        # first thought is sort index in indices, mark as True if we can replace
        # then build string bottom up
        res = []
        j = 0
        boolean_arr = [False] * len(s)
        hashmap = {}
        for i in range(len(indices)):
            
            target_string = sources[i]
            start_idx = indices[i]
            if s[start_idx:start_idx+len(target_string)] == target_string:
                hashmap[start_idx] = (targets[i], sources[i])
            
        i = 0
        while i < len(s):
            if i in hashmap:
                res.append(hashmap[i][0])
                i += len(hashmap[i][1])
            else:
                res.append(s[i])
                i += 1
        print(res)
        return ''.join(res)