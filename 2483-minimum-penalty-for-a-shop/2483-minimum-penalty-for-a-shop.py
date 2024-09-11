class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        # array of customer visits - Y = visit, N = No visit
        # if shop is closed and and customers come penalty += 1
        # if shop is open and customers dont come penalty += 1
        
        # pick earliest time to have minimum penalty
        
        # intuition tells me a suffix problem?
        # maybe build right to left, check penalty at every index if shop is open or closed
        
        # ex for YYNY
    
        # tuple = (penalty)
        '''
        [0] = count of Ys [0:] + 0
        [1] = count of Ys [1:] + count of Ns[:1]
        [2] = 
        
        count_of_y = [3,2,1,1,0]
        count_of_n = [0,0,0,1,1]
        '''
        
        
        # just count y and ns as we traverse right to left and calculate?
        # count ys from right to left
        # count ns from left to right
        # calculate min for these from right to left
        
        min_result = float("inf")
        n_counts = [0] * (len(customers) + 1)
        y_counts = [0] * (len(customers) + 1)
        for i in range(1, len(customers)+1):
            if customers[i-1] == 'N':
                count = 1
            else:
                count = 0
            n_counts[i] = n_counts[i-1] + count
            
        for i in range(len(customers)-1, -1, -1):
            if customers[i] == 'Y':
                count = 1
            else:
                count = 0
            y_counts[i] = y_counts[i+1] + count
        
        min_count = min(y_counts[i] + n_counts[i] for i in range(len(n_counts)))
        for i in range(len(n_counts)):
            if n_counts[i] + y_counts[i] == min_count:
                return i 
        
        return -1
        