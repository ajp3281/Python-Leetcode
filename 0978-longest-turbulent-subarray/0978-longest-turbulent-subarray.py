class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        # start new arr from current index
        # how do we know which condition to even take?

        # can we take either condition? looks like it
        # check starting condition and track prev sign as we iterate

        if len(arr) == 1:
            return 1
        if len(arr) == 2:
            if arr[1] != arr[0]:
                return 2
            else:
                return 1
        left = 0
        if arr[0] == arr[1]:
            prevsign = '!'
            left = 1
        elif arr[0] < arr[1]:
            prevsign = '<'
        else:
            prevsign = '>'
        
        maxlen = 0 

        for r in range(1, len(arr)-1):
            if prevsign == '<':
                if arr[r] < arr[r+1]:
                    left = r
                elif arr[r] == arr[r+1]:
                    left = r + 1
                else:
                    prevsign = '>'
            else:
                if arr[r] > arr[r+1]:
                    left = r
                elif arr[r] == arr[r+1]:
                    left = r + 1
                else:
                    prevsign = '<'
            maxlen = max(r - left + 1, maxlen)

        print(left)
        return maxlen + 1
        