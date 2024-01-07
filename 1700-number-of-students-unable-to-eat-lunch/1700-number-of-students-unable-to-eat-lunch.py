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
                
        