class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # why dont we use a stack instead
        # add first character 
        # if next character is almost equal, pop from stack and skip current
        # and increase res by 1

        int_word = [ord(char) - 97 for char in word]

        def almost_equal(a,b):
            if a == 0:
                return (b == 0 or b == 26 or b == 1)
            elif b == 0:
                return (a == 0 or a == 26 or a == 1)

            return (abs(a-b) <= 1)

        stack = []
        stack.append(int_word[0])
        res = 0
        for i in range(1, len(int_word)):
            current = int_word[i]

            if stack and almost_equal(current, stack[-1]):
                res += 1
                stack.pop()
                stack.append("ZZZ")
            else:
                stack.append(current)

        return res