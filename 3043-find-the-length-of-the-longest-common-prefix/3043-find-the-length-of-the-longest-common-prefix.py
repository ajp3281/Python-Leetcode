class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # store all prefixes in a set and then do the comparing
        
        # 100
        # 0
        prefix_set = set()
        for num in arr1:
            num_str = str(num)
            for j in range(len(num_str)):
                prefix_set.add(num_str[:j+1])
                
        prefix_set_2 = set()
        for num in arr2:
            num_str = str(num)
            for j in range(len(num_str)):
                prefix_set_2.add(num_str[:j+1])
                
        
                
        # how to compare prefixes with other?
        res = 0
        for num in prefix_set:
            if num in prefix_set_2:
                res = max(res, len(num))
        return res

        '''
        string_arr_1 = []
        string_arr_2 = []
        # remove dupes, maybe check if index == max length string in arr2, sort by reverse length once we find one that reaches max length of word, that has to be the longest?
        # check every elem in arr1 with elem in arr2
        for num in arr1:
            string_arr_1.append(str(num))
        for num in arr2:
            string_arr_2.append(str(num))
        res = 0
        for i in range(len(string_arr_1)):
            for j in range(len(string_arr_2)):
                left_num = string_arr_1[i]
                right_num = string_arr_2[j]
                
                index = 0
                while index < min(len(left_num), len(right_num)) and left_num[index] == right_num[index]:
                    index += 1
                res = max(index, res)
        return res
        '''
        