class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        # build all prefixes for each word
        # map the list to the index
        # ex:
        # abc, ab, bc, b
        # [a, ab, abc], [a, ab], [b, bc], [b]
        #.     0.          1        2.     3
        # store count of how many times each prefix appears overall in a hashmap?
        # a = 2, ab = 2, b = 2, bc = 2, abc = 1
        # then iterate thru all possible prefixes for each string and add the count
        res = [0] * len(words)
        prefixes = {}
        for word in words:
            for j in range(len(word)):
                current_prefix = word[:j+1]
                if current_prefix in prefixes:
                    prefixes[current_prefix] += 1
                else:
                    prefixes[current_prefix] = 1
 
        for i, word in enumerate(words):
            for j in range(len(word)):
                current_prefix = word[:j+1]
                res[i] += prefixes[current_prefix]
                
        return res
            
        