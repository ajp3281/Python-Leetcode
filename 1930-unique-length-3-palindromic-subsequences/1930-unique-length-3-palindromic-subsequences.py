from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        # character counter
        # iterate left to right
        # if count of current character > 1, increase right until we reach it
        # count unique subsequences we pass by
        # decrease count of left and keep iterating

        count = Counter(s)
        visited = set()
        for char in count.keys():
            if count[char] > 2:
                visited.add(char)
        left = 0
        while left < len(s)-2:

            if count[s[left]] > 1:

                right = left + 1

                while s[right] != s[left]:
                    subseq = s[left] + s[right] + s[left]
                    if subseq not in visited:
                        visited.add(subseq)

                    right += 1

            count[s[left]] -= 1
            if count[s[left]] == 0:
                count.pop(s[left])

            left += 1

        return len(visited)
        