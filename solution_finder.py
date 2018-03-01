from utils import distance_between_points


class Ride(object):
    def __init__(self, id, i_x, i_y, i_t, f_x, f_y, f_t):
        self.id = id
        self.i_x = i_x
        self.i_y = i_y
        self.i_t = i_t
        self.f_x = f_x
        self.f_y = f_y
        self.f_t = f_t

    def get_points(self):
        return distance_between_points(self.i_x, self.i_y, self.f_x, self.f_y)


class SolutionFinder(object):
    current_car = 0
    max_points = 0
    rides = []

    def __init__(self, num_cars, bonus, time_steps, num_rows, num_cols):
        self.num_cars = num_cars
        self.cars = [[] for i in range(num_cars)]
        self.bonus = bonus
        self.time_steps = time_steps
        self.num_rows = num_rows
        self.num_cols = num_cols

    def initialize_max_points(self):
        self.max_points = 0

        for ride in self.rides:
            self.max_points += ride.get_points()

        self.max_points += self.bonus * len(self.rides)

    def add_ride(self, id, i_x, i_y, i_t, f_x, f_y, f_t):
        ride = Ride(id, i_x, i_y, i_t, f_x, f_y, f_t)
        self.rides.append(ride)
        self.assign_ride_to_car(ride)

    def assign_ride_to_car(self, ride):
        self.cars[self.current_car].append(ride)

        self.current_car += 1
        self.current_car %= self.num_cars

    def __str__(self):
        for i in range(len(self.cars)):
            rides_str = ""
            for ride in self.cars[i]:
                rides_str += "{0} ".format(ride.id)

            print("{0} {1}".format(len(self.cars), rides_str))

    def calculate_ride_points(self, car, ride, position, step):

        distance_to_start = distance_between_points(position[0], position[1], ride.i_x, ride.i_y)
        ride_distance = distance_between_points(ride.i_x, ride.i_y, ride.f_x, ride.f_y)

        points = 0

        ride_is_possible = step + distance_to_start + ride_distance < ride.f_t
        early_arrival_is_possible = step + distance_to_start < ride.i_t

        if ride_is_possible:
            points = ride_distance
            step += distance_to_start + ride_distance
            position = (ride.f_x, ride.f_y)

            if early_arrival_is_possible:
                points += self.bonus

        return points, position, step

    def get_car_points(self, car):
        points = 0
        position = (0, 0)
        step = 0
        for ride in car:
            ride_points, position, step = self.calculate_ride_points(car, ride, position, step)

            if step > self.time_steps:
                return points

            points += ride_points

        return points

    def get_points(self):
        points = 0
        for car in self.cars:
            points += self.get_car_points(car)
        return points

    def get_heuristic(self):
        return self.max_points - self.get_points()
