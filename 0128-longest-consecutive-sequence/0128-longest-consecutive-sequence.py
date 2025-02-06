class UnionFind:
    def __init__(self):
        self.par = {}
        self.rank = {}

    def find(self, n):
        if n not in self.par:
            self.par[n] = n
            self.rank[n] = 0
        if self.par[n] == n:
            return n
        par = self.par[n]
        self.par[n] = self.find(par)
        return self.par[n]

    def union(self, n1, n2):
        par1, par2 = self.find(n1), self.find(n2)
        
        if self.rank[par1] >= self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += 1
        else:
            self.par[par1] = par2
            self.rank[par2] += 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        uf = UnionFind()
        visited = set()
        for num in nums:
            if num-1 in visited:
                uf.union(num-1, num)
            if num+1 in visited:
                uf.union(num + 1, num)
            visited.add(num)

        for num in nums:
            uf.par[num] = uf.find(num)

        values_list = list(uf.par.values())
        counter = Counter(values_list)
        print(counter)
        return max(counter.values())
        #max_elem = max(values_list, key=values_list.count)

        return values_list.count(max_elem) 