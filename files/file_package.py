def sum_file(a, b, filename='sum.txt'):
    result = a + b # int
    with open(filename, 'w') as file:
        file.write(str(result))

def read_sum_file(filename='sum.txt'):
    with open(filename, 'r') as file:
        return int(file.read())
