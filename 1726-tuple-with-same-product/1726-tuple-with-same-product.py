class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        # every 4 numbers that combine for same product = 8 tuples
        # store products in a map and iterate while keeping track of dupes?

        products = {}
        res = 0
        seen = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (i,j) not in seen and (j,i) not in seen:
                    products[nums[i] * nums[j]] = products.get(nums[i] * nums[j], 0) + 1
                    seen.add((i,j))

        # this wont work for combinations right
        print(products)
        # if products is 3 how many combinations of tuples can we make?
        # 
        #4 means?
        #3 means 24
        #2 means = 8 combinations
        # 2 means * 4
        # 3 means * 8
        # 4 means * 16

        #
        count = 0
        for val in products.keys():
            n = products[val]
            res += int((n*(n-1))/2)
        
        return res * 8
        