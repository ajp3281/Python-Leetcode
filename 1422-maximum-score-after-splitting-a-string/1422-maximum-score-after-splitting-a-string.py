class Solution:
    def maxScore(self, s: str) -> int:
        
        # count 1s and 0s, subtract/add score as we see them?

        ones = 0
        zeroes = 0

        for char in s:
            if char == "1":
                ones += 1
            else:
                zeroes += 1

        right = ones
        left = 0
        maxscore = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                left += 1
            elif s[i] == "1":
                right -= 1
            print(i, left, right, maxscore)
            maxscore = max(maxscore, left + right)

        return maxscore
