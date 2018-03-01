class Ride(object):
    def __init__(self, id, i_x, i_y, i_t, f_x, f_y, f_t):
        self.id = id
        self.i_x = i_x
        self.i_y = i_y
        self.i_t = i_t
        self.f_x = f_x
        self.f_y = f_y
        self.f_t = f_t


class SolutionFinder(object):
    current_car = 0

    def __init__(self, num_cars, bonus, time_steps, num_rows, num_cols):
        self.num_cars = num_cars
        self.cars = [[] for i in range(num_cars)]
        self.bonus = bonus
        self.time_steps = time_steps
        self.num_rows = num_rows
        self.num_cols = num_cols

    def add_ride(self, id, i_x, i_y, i_t, f_x, f_y, f_t):
        ride = Ride(id, i_x, i_y, i_t, f_x, f_y, f_t)
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
