class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        # dfs - keep track of index and current strog number
        # right index must be equal to strog number
        # middle can map to itself?
        
        # backtracking solution , need to check every possibility
        # start with every strog number -
        
        if n == 1:
            return ["0","1","8"]
        
        strog_map = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6',
        }

        res = []
        def helper(index, path):
            if index == n:
                print(path)
                res.append(''.join(path.copy()))
                return
            
            # check if middle element, or if in 2nd half and need to match to first half
            # also need to take care of 0s, cant come in beginning
            # still need to add check for middle element in odd length n
            left = n - index - 1
            if n % 2 != 0 and index == n//2:
                for key in strog_map.keys():
                    if key == strog_map[key]:
                        path.append(str(strog_map[key]))
                        helper(index + 1, path)
                        path.pop()
            elif index >= (n//2):
                path.append(strog_map[path[left]])
                helper(index + 1, path)
                path.pop()
            else: 
                for key in strog_map.keys():
                    if index == 0 and key == '0':
                        continue
                    path.append(str(strog_map[key]))
                    helper(index + 1, path)
                    path.pop()
        helper(0,[])
        return res
            
        
        
        