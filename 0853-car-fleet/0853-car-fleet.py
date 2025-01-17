class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # check and sort by times and position?
        cars = []
        for i in range(len(position)):
            cars.append((position[i], (target - position[i])/speed[i]))

        cars.sort()
        print(cars)

        # if time[i] < time[i+1]

        i = len(cars)-1
        fleets = 0
        while i >= 0:
            time = cars[i][1]
            while i > 0 and time >= cars[i-1][1]:
                time = max(time, cars[i-1][1])
                i -= 1
            fleets += 1
            i -= 1

        return fleets