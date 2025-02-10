class Solution:
    def clearDigits(self, s: str) -> str:

        # stack approach
        # add all non digits to stack
        # if we see a digit, continue and pop from the stack
        # return joined stack
        stack = []
        for char in s:
            if char.isalpha():
                stack.append(char)
            else:
                stack.pop()
        return ''.join(stack)
        