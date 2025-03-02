class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        key_to_id = defaultdict(int)
        for num in nums1:
            key_to_id[num[0]] += num[1]

        for num in nums2:
            key_to_id[num[0]] += num[1]

        res = []
        for i in range(1001):
            if i in key_to_id:
                res.append([i, key_to_id[i]])
        return res
        