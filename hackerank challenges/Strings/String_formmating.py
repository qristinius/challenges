def print_formatted(number):
    
    width = len(str(bin(number)[2:]))
    for i in range (1, number+1):
        print(str(i).rjust(width," ") , oct(i)[2:].rjust(width," "), hex(i).upper()[2:].rjust(width," "), bin(i)[2:].rjust(width," "))
        

#way beautiful code
""" 	
def print_formatted(number):
	    '''Prints number in decinmal, ocal, hexadecimal, and binary'''
	    for i in range(1, number + 1):
	        width = len(f"{number:b}")
	        print(f"{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}")
	 """



    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)