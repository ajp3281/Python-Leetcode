class NumberContainers:
    # num to idx mapping
    # how to keep track of current minimum index for that number?
    # heap? - we can't pop middle elements in time
    # instead of pop just keep track?
    # visited set for (num,idx)? 
    # keep popping from heap until num,idx not in visited set
    # should be idx -> num - to be able to replace

    def __init__(self):
        self.idx_to_num = {}
        self.num_to_idx_heap = {}
        self.version = 0

    def change(self, index: int, number: int) -> None:
        self.version += 1
        new_version = self.version
        # if we are replacing an existing number at this index - mark it
        if index in self.idx_to_num and self.idx_to_num[index][0] == number:
            return 

        # append idx into list of indexes for this number
        if number not in self.num_to_idx_heap:
            self.num_to_idx_heap[number] = [(index, new_version)]
            heapq.heapify(self.num_to_idx_heap[number])

        else:
            heapq.heappush(self.num_to_idx_heap[number], (index, new_version))

        # replace number at this index
        self.idx_to_num[index] = (number, new_version)
        

    def find(self, number: int) -> int:
        #print(self.num_to_idx_heap)
        if number not in self.num_to_idx_heap:
            return -1
        
        while self.num_to_idx_heap[number]:
            idx, version = self.num_to_idx_heap[number][0]
            if idx in self.idx_to_num and (number, version) == self.idx_to_num[idx]:
                return idx
            else:
                heapq.heappop(self.num_to_idx_heap[number])



        return -1




# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)