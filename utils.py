from solution_finder import SolutionFinder


def read_file(file_path):
    file = open(file_path, 'r')

    # READ FIRST LINE
    # 3 4 2 3 2 10 -> 3 rows, 4 columns, 2 vehicles, 3 rides, 2 bonus and 10 steps
    lines = file.readlines()
    first_line = lines.pop(0).split(" ")

    num_rows = int(first_line[0])
    num_cols = int(first_line[1])
    num_cars = int(first_line[2])
    # num_rides = int(first_line[3])
    bonus = int(first_line[4])
    time_steps = int(first_line[5])

    # Initialize solution
    initial_solution = SolutionFinder(num_cars, bonus, time_steps, num_rows, num_cols)

    # Read others solution
    # 0 0 1 3 2 9 -> ride from [0, 0] to [1, 3], earliest start 2, latest finish 9
    for i in range(len(lines)):
        line = lines[i].split(" ")
        print(line)

        i_x = int(line[0])
        i_y = int(line[1])
        f_x = int(line[2])
        f_y = int(line[3])
        i_t = int(line[4])
        f_t = int(line[5])

        initial_solution.add_ride(i, i_x, i_y, i_t, f_x, f_y, f_t)

    initial_solution.initialize_max_points()
    return initial_solution


def distance_between_points(i_x, f_x, i_y, f_y):
    return abs(f_x - i_x) + abs(f_y - i_y)
