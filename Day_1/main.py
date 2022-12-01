def readFile(path):
    with open(path) as f:
        contents = f.read()
        return contents

def getTopCalories():
    data = readFile("./input.txt")
    data = str(data).split("\n\n")
    sum_data = []
    for items in data:
        new_data = items.split("\n")
        sum_data.append(sum([int(x) for x in new_data]))
    output = max(sum_data)
    print(output)  
    return output

def getBestThreeCalories(n=3):
    data = readFile("./input.txt")
    data = str(data).split("\n\n")
    sum_data = []
    for items in data:
        new_data = items.split("\n")
        sum_data.append(sum([int(x) for x in new_data]))
    sum_data.sort(reverse=True)  
    output = sum(sum_data[0:n])
    print(output)  
    return output

def main():
    """ Main program """
    getTopCalories()
    getBestThreeCalories(3)

if __name__ == "__main__":
    main()