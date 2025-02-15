class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(i, n_list, target, current, current_partition):
            #print(i, current, current_partition)

            if current + current_partition == target and i == len(n_list):
                return True
            if current + current_partition > target or i >= len(n_list):
                return False

            # how to handle starting new list vs keeping?
            take_val = (current_partition * 10) + n_list[i]
            
            # how to handle storing vals?
        
            take = partition(i + 1, n_list, target, current, take_val)
            skip = partition(i + 1, n_list, target, current + current_partition, n_list[i])

            return take or skip
        # can we be greedy in our partitions?
        # dp works?
        # lets go dp first
        res = 0
        for i in range(1, n + 1):
            i_list = [int(num) for num in str(i**2)]
            if partition(1, i_list, i, 0, i_list[0]):
                res += i**2
        return res              

            
            

        