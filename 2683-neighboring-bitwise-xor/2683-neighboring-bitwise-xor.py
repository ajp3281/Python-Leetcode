class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        # start at first and last?
        # if derived[-1] = 0:
        # original[0] = 0 and original[-1] = 0 or origina[0] = 1 and original[-1] = 1

        # do everything except first and last?

        # every elem is used twice, meaning now 
        check = 0
        for derive in derived:
            check ^= derive
        for i in range(2,len(derived)):
            if derived[i] == derived[i-1] and derived[i] == derived[i-2] and check == 1:
                return False
        return check == 0