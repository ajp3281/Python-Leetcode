class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # window length - maxfreq = replacements needed
        # result only increases if we are in valid state and maxfreq increases
        # we don't even need a maxlength tracker
        # increase right ptr if we are in a valid state
        # else increase left

        l = 0
        maxfreq = 0
        counts = [0] * 26
        for r in range(len(s)):
            print(l,r, maxfreq)
            window = r - l + 1
            counts[ord(s[r]) - ord('A')] += 1
            maxfreq = max(maxfreq, counts[ord(s[r]) - ord('A')])

            while l <= r and window - maxfreq > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1

        return min(maxfreq + k, len(s))
