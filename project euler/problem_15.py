import math as m

def finding_unique_route(grid):
    # formula for combinatorics that counts unique ways to move from upper left corner
    # of the grid to the rightermost
    routenum = int((m.factorial(2*grid))/(m.factorial(grid) * m.factorial(grid)))
    return routenum

finding_unique_route(20)