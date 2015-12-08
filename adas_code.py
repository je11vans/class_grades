def read_data(file):
    infile = open(file,'r')
    numbers = []
    for line in infile:
        values = line.split(",") 
        numbers.append(int(values[1]))

    return numbers
