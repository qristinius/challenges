if __name__ == '__main__':
    s = input() 
    #list comperhension + any fnction 
    #any functions prints true if any of the following list item is true else it prints false 
    print(any([i.isalnum() for i in s]) )
    print(any([i.isalpha() for i in s]) )
    print(any([i.isdigit() for i in s]) )
    print(any([i.islower() for i in s]) )
    print(any([i.isupper() for i in s]) )