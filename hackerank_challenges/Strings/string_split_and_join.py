#splitting strings into spaces and putting anything ("- " this thing in that case) where spaces should be 
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)