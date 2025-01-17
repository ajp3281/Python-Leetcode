class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        # just count all and shift once?
        left = 0
        right = 0
        for shi in shift:
            if shi[0] == 0:
                left -= shi[1]
            else:
                right += shi[1]

        res = right + left

        # shift 3 
        # abcdefg
        # 0123456
        # efg + abcd
        # s[right+1:] + s[:right+1]

        # defg + abc
        # s[]

        # shift 1
        # mecsk
        # s[right+1:] + s[:res+1]
        res %= len(s)
        print(res)
        if res > 0:
            return s[len(s) - res:] + s[:len(s)-res]
        else:
            # shift left 4
            left = res*-1
            return s[left:] + s[:left]
        