class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        # seems like another stack problem
        
        # add index to stack if we dont need to pop
        # if current index == top of stack we need to pop
        #   res += neededTime[poppedidx]

        # but we need min time - can we be greedy when we choose which one to pop?

        # we know one of them needs to be popped so lets choose min?
        stack = []
        res = 0
        for i, c in enumerate(colors):
            if not stack or c != stack[-1][0]:
                stack.append((c, neededTime[i]))

            else:
                popped_color, poppedTime = stack.pop()
                stack.append((c, max(neededTime[i], poppedTime)))
                res += min(neededTime[i], poppedTime)
        return res
