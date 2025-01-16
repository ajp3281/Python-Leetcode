class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        nums3 = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                nums3.append(nums1[i] ^ nums2[j])

        res = 0
        for num in nums3:
            res ^= num

        return res

        


        