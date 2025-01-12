class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        prefix = [0]
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])

        res = []
        # count how many times every idx appears?
        for query in queries:
            left = query[0]
            right = query[1]
            
            current = prefix[right+1] - prefix[left]

            res.append(current)

        return res

        # prefix sums?
        # prefix = 0,1,1,2,3,4
        # 

        '''
        for i in range(len(vowel_strings)):
            if vowel_strings[i] == True:
                res += 
        '''

        