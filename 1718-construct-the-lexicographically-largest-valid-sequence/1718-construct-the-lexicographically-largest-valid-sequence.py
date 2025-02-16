class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        
        # backtracking but place elem twice every time!!
        sequence = [0] * (2 * n - 1)
        res = []
        def backtrack(idx, used):
            if idx == len(sequence):
                return True

            for num in reversed(range(1, n + 1)):
                # should we just place first?
                if num in used:
                    continue
                if (num != 1) and (num + idx >= len(sequence) or sequence[num+idx] != 0):
                    continue
                
                sequence[idx] = num
                if num != 1:
                    sequence[idx + num] = num
                used.add(num)

                prev_idx = idx
                while idx < len(sequence) and sequence[idx] != 0:
                    idx += 1

                if backtrack(idx, used):
                    return True

                sequence[prev_idx] = 0
                if num != 1:
                    sequence[prev_idx + num] = 0
                used.remove(num)

            return False

        backtrack(0, set())
        return sequence