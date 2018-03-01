from utils import read_file

input = input("Enter input file (a, b, c, d):")

print("Selected input: ", input)

file_path = '{0}_example.in'.format(input)
initial_solution = read_file(file_path)
