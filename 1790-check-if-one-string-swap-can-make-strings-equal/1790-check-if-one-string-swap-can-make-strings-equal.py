class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        set1, set2 = Counter(s1), Counter(s2)
        if set1 != set2:
            return False
        mismatches = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatches += 1

        return mismatches <= 2
        