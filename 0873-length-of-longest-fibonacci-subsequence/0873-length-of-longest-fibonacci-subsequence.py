class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        # Create a mapping from value to its index for O(1) lookups.
        index = {num: i for i, num in enumerate(arr)}
        # dp[i, j] will store the length of the Fibonacci-like sequence ending with arr[i] and arr[j].
        dp = {}
        res = 0

        # Loop over pairs (i, j) with i < j.
        for j in range(n):
            for i in range(j):
                # The number that should come before arr[i] in the sequence is:
                # prev = arr[j] - arr[i]
                prev = arr[j] - arr[i]
                # Check that prev is less than arr[i] (guaranteed if the array is strictly increasing)
                # and that it exists in the array.
                if prev < arr[i] and prev in index:
                    k = index[prev]
                    # If there's an existing sequence ending with (k, i), extend it.
                    dp[i, j] = dp.get((k, i), 2) + 1
                    res = max(res, dp[i, j])
                else:
                    # Otherwise, the pair (i, j) forms a sequence of length 2.
                    dp[i, j] = 2

        return res if res >= 3 else 0

        