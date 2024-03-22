class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sort all the words and use as key for hashmap - 
        stringmap = defaultdict(list)
        for word in strs:
            sortedword = ''.join(sorted(word))
            stringmap[sortedword].append(word)
            
            
        print(stringmap)
        
        res = []
        for key in stringmap.keys():
            res.append(stringmap[key])
        
        return res
            
            
            
            
        