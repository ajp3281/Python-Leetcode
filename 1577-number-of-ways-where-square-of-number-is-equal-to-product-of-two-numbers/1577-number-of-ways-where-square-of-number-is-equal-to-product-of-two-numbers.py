class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        type1 = defaultdict(int)
        type2 = defaultdict(int)
        for i in range(len(nums1)):
            type1[nums1[i]**2] += 1
        for i in range(len(nums2)):
            type2[nums2[i]**2] += 1


        for j in range(len(nums2)):
            for x in range(j + 1, len(nums2)):
                if nums2[j] * nums2[x] in type1:
                    res += type1[nums2[j] * nums2[x]]

        for j in range(len(nums1)):
            for x in range(j + 1, len(nums1)):
                if nums1[j] * nums1[x] in type2:
                    res += type2[nums1[j] * nums1[x]]
        
        return res
        