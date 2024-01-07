# o(n^2) time using queue - worst case need to check every student every time you reach new sandwich - can be improved by not using queue
# o(n) space - o(2n) because 2 queues but rounds down to o(n) - can be done in o(1) without using queue
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        q = deque(students)
        sand = deque(sandwiches)
        while q:
            ate = False
            for i in range(len(q)):
                print(q[0], sand[0])
                if q[0] == sand[0]:
                    q.popleft()
                    sand.popleft()
                    ate = True
                else:
                    q.append(q.popleft())
            if ate == False:
                return len(q)
        
        return 0
                
        