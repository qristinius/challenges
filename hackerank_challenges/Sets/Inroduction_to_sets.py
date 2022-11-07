def average(array):
    # your code goes here
    distinct_height = set(arr)
    len_array = len(distinct_height)
    
    avrage_height = sum(distinct_height) / len_array
    return avrage_height

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)