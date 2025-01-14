class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        

        # numbers present at or before idx
        # how to keep track of what we've visited?

        # at idx 0 - check if match, if so increase by 1?
        # how do we go backwards to check if we've seen?
        # just do visited set for now?

        # visited set window??
        # how to use permutations to our advantage

        res = [0]
        visited_A = set()
        visited_B = set()
        for i in range(len(A)):
            
            next_num = 0
            if A[i] == B[i]:
                next_num += 1
            else:
                visited_A.add(A[i])
                visited_B.add(B[i])
                if A[i] in visited_B:
                    next_num += 1
                if B[i] in visited_A:
                    next_num += 1
            res.append(res[-1] + next_num)

        return res[1:]



