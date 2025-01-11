from collections import Counter
class Solution:
    # how can we improve time complexity?
    # combine all words in words2 into one big word
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word2_map = [0] * 26
        for word2 in words2:
            counter2 = Counter(word2)
            for character in counter2.keys():
                idx = ord(character) - ord('a')
                if word2_map[idx] == 0:
                    word2_map[idx] = counter2[character]
                else:
                    word2_map[idx] = max(word2_map[idx], counter2[character])

        def isSubset(a, word2_map):
            counter_a = Counter(a)
            for i in range(len(word2_map)):
                if word2_map[i] != 0:
                    char_idx = i + ord('a')
                    char = chr(char_idx)
                    if char not in counter_a or word2_map[i] > counter_a[char]:
                        return False
            return True

        res = []
        for word in words1:
            flag = True
            if not isSubset(word, word2_map):
                flag = False
                continue
            if flag:
                res.append(word)
        return res

        