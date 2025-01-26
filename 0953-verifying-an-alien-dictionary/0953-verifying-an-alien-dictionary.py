class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # compare adj words

        charToVal = {}
        for i,char in enumerate(order):
            charToVal[char] = i

        for i in range(len(words)-1):
            prev_word, next_word = words[i], words[i+1]

            for j in range(len(prev_word)):

                if j >= len(next_word) or charToVal[next_word[j]] < charToVal[prev_word[j]]:
                    return False
                elif charToVal[next_word[j]] > charToVal[prev_word[j]]:
                    break

        return True
                

        