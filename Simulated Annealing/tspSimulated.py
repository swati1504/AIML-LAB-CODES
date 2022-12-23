import sys
import random
import copy
import numpy as np

class State:
    # Create a new state
    def __init__(self, route:[], distance:int=0):
        self.route = route
        self.distance = distance
    # Compare states
    def __eq__(self, other):
        for i in range(len(self.route)):
            if(self.route[i] != other.route[i]):
                return False
        return True
    # Sort states
    def __lt__(self, other):
         return self.distance < other.distance
    # Print a state
    def __repr__(self):
        return ('({0},{1})\n'.format(self.route, self.distance))

    def copy(self):
        return State(self.route, self.distance)

    def deepcopy(self):
        return State(copy.deepcopy(self.route), copy.deepcopy(self.distance))

    def update_distance(self, matrix, home):
        # Reset distance
        self.distance = 0
        # Keep track of departing city
        from_index = home
        for i in range(len(self.route)):
            self.distance += matrix[from_index][self.route[i]]
            from_index = self.route[i]
        # Add the distance back to home
        self.distance += matrix[from_index][home]
# This class represent a city (used when we need to delete cities)
class City:
    # Create a new city
    def __init__(self, index:int, distance:int):
        self.index = index
        self.distance = distance
    # Sort cities
    def __lt__(self, other):
         return self.distance < other.distance
# Return true with probability p
def probability(p):
    return p > random.uniform(0.0, 1.0)
# Schedule function for simulated annealing
def exp_schedule(k=20, lam=0.005, limit=1000):
    return lambda t: (k * np.exp(-lam * t) if t < limit else 0)

def get_best_solution_by_distance(matrix:[], home:int):
    route = []
    from_index = home
    length = len(matrix) - 1
    # Loop until route is complete
    while len(route) < length:
        row = matrix[from_index]
        cities = {}
        for i in range(len(row)):
            cities[i] = City(i, row[i])
        del cities[home]
        for i in route:
            del cities[i]
        # Sort cities
        sorted = list(cities.values())
        sorted.sort()
        # Add the city with the shortest distance
        from_index = sorted[0].index
        route.append(from_index)
    state = State(route)
    state.update_distance(matrix, home)
    return state

def mutate(matrix:[], home:int, state:State, mutation_rate:float=0.01):
    # Create a copy of the state
    mutated_state = state.deepcopy()
    for i in range(len(mutated_state.route)):
        if(random.random() < mutation_rate):
            # Swap two cities
            j = int(random.random() * len(state.route))
            city_1 = mutated_state.route[i]
            city_2 = mutated_state.route[j]
            mutated_state.route[i] = city_2
            mutated_state.route[j] = city_1
    mutated_state.update_distance(matrix, home)
    return mutated_state

def simulated_annealing(matrix:[], home:int, initial_state:State, mutation_rate:float=0.01, schedule=exp_schedule()):
    best_state = initial_state
    for t in range(sys.maxsize):
        T = schedule(t)
        if T == 0:
            return best_state
        neighbor = mutate(matrix, home, best_state, mutation_rate)
        delta_e = best_state.distance - neighbor.distance
        if delta_e > 0 or probability(np.exp(delta_e / T)):
            best_state = neighbor

def main():
    # Cities
    cities = ['Bucharest', 'Zerind', 'Neamt', 'Petisti', 'Fagaras', 'Atlantis', 'Seattle', 'Boston', 'San Francisco', 'St. Louis', 'Houston', 'Phoenix', 'Salt Lake City']
    city_indexes = [0,1,2,3,4,5,6,7,8,9,10,11,12]

    home = 2 
    # Distances in miles between cities
    matrix = [[0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
            [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
            [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
            [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
            [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
            [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
            [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
            [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
            [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
            [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
            [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
            [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
            [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0]]
    # Get the best route by distance
    state = get_best_solution_by_distance(matrix, home)
    print('Best solution by distance')
    print(cities[home], end='')
    for i in range(0, len(state.route)):
       print(' -> ' + cities[state.route[i]], end='')
    print(' -> ' + cities[home], end='')
    print('\n\nTotal distance: {0} miles'.format(state.distance))
    print()
    # Run simulated annealing to find a better solution
    state = get_best_solution_by_distance(matrix, home)
    state = simulated_annealing(matrix, home, state, 0.1)
    print('Simulated annealing solution')
    print(cities[home], end='')
    for i in range(0, len(state.route)):
       print(' -> ' + cities[state.route[i]], end='')
    print(' -> ' + cities[home], end='')
    print('\n\nTotal distance: {0} miles'.format(state.distance))
    print()

if __name__ == "__main__": main()
