# sometimes you just have to sort a list
# when given multiple lists, putting them into a list of tuples then sorting can help

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # define data structures
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars = sorted(cars)
        fleet_time = (target - cars[-1][0]) / cars[-1][1]
        fleets = 1

        for i in range(len(position) - 2, -1, -1):
            car_time = (target - cars[i][0]) / cars[i][1]

            if car_time > fleet_time:
                fleets += 1
                fleet_time = car_time 
        
        return fleets