from itertools import product

# number of lists and final_mode valuenp
number_of_lists, final_mode = map(int, input().split())

lists = [list(map(int, input().split()))[1:] for _ in range(number_of_lists)]

# maximum modulo value
max_modulo = 0

# iterating through all combinations of one element from each list
for combination in product(*lists):
    # the sum of squares modulo final_mode
    current_modulo = sum(x**2 for x in combination) % final_mode
    # the maximum modulo value if needed
    max_modulo = max(max_modulo, current_modulo)

# the maximum modulo value
print(max_modulo)
