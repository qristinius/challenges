year = int(input())

def is_leap(year):
    if year % 4 == 0 :
        leap = True
    else:
        leap = False

    return leap