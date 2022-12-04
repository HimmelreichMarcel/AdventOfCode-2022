
def partOne():
    file1 = open('./input.txt', 'r')
    lines = file1.readlines()
    sum = 0
    for line in lines:
        line = line.strip()
        first, second = line.split(',')
        first_min, first_max = first.split('-')
        second_min, second_max = second.split('-')
        if (int(first_min) <= int(second_min) and int(first_max) >= int(second_max)) or (int(second_min) <= int(first_min) and int(second_max) >= int(first_max)):
            sum += 1
    return sum

def partTwo():
    file1 = open('./input.txt', 'r')
    lines = file1.readlines()
    sum = 0
    for line in lines:
        line = line.strip()
        first, second = line.split(',')
        first_min, first_max = first.split('-')
        second_min, second_max = second.split('-')
        if int(first_max) < int(second_min) or int(first_min) > int(second_max):
            sum += 1
    return len(lines) - sum

def main():
    """ Main program """
    result = partOne()
    print(result)
    result = partTwo()
    print(result)
    
if __name__ == "__main__":
    main()