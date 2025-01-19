class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start from the middle checking odd and even lengths
        def helper(lo, hi):
            # lo,hi=2
            # 
            while lo >= 0 and hi <= len(s)-1:
                if s[lo] == s[hi] and lo - 1 >= 0 and hi + 1 <= len(s)-1:
                    lo -= 1
                    hi += 1
                else:
                    break

                #print(lo,hi)

            if lo >= 0 and hi <= len(s) - 1 and s[lo] != s[hi]:
                lo += 1
                hi -= 1
            return s[lo:hi+1]

        res = ""
        for i in range(len(s)):
            odd = helper(i,i)
            even = helper(i, i+1)
            print(i, odd, even)
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res