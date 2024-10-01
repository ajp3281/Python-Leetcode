class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # 2 ptr approach to build pairs?
        # maybe calculate remainder of 5 and store in arr
        # see if we have a match?
        
        # 1,2,3,4,5,6
        # 1=6, 2=5, 3=4,4=3,5=2,6=1?
        # or maybe flip by remainder and pop like that for o(1) search
        
        # 6=1, 5=2, 4=3,3=4, 2=5, 6=1
        # verify count of keys are equal?
        # so for len(6) == len(1), continue
        # if not a match return False
        
        # how to handle negative numbers?
        # 0 is also divisible by every num
        

        hashmap = defaultdict(int)
        for num in arr:
            hashmap[num % k] += 1
        print(hashmap)
        for i in range(k):
            if i == 0:
                if hashmap[i] % 2 != 0:
                    return False
            else:
                if hashmap[abs(i)] != hashmap[abs(k-i)]:
                    return False
        return True
        