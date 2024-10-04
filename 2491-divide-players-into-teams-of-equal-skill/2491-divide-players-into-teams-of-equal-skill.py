class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # can we sort and be greedy?
        # 18
        # 3,3, 5,1 4,2
        
        sorted_skills = sorted(skill)
        left = 0
        right = len(sorted_skills) - 1
        
        target = sorted_skills[right] + sorted_skills[left]
        res = 0
        while left <= right:
            if sorted_skills[right] + sorted_skills[left] != target:
                return -1
            
            res += sorted_skills[right] * sorted_skills[left]
            left += 1
            right -= 1
            
        return res