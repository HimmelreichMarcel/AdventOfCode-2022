import os
import json

map = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

def splitString(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2


def stringStack(stack: str):
    stack = stack.split('\n')
    return stack[0], stack[1], stack[2]

def readFile(path):
    with open(path) as f:
        contents = f.read()
        return contents
    
def findMatch(first, second, third=None):
    if third:
        for letter1 in first:
            for letter2 in second:
                for letter3 in third:
                    if letter1 == letter2 and letter2 == letter3:
                        return letter1
    for letter1 in first:
        for letter2 in second:
                if letter1 == letter2:
                    return letter1
    return first

def partOne():
    file1 = open('./input.txt', 'r')
    Lines = file1.readlines()
    sum = 0
    for line in Lines:
        first, second = splitString(line)
        match = findMatch(first, second)
        if not match:
            continue
        sum += map.get(match)
    return sum

def partTwo():
    file1 = open('./input.txt', 'r')
    Lines = file1.readlines()
    sum = 0
    index = 0
    temp_file = ""
    for line in Lines:
        temp_file += line
        if index % 2 == 0 and index != 0:
            temp_file += '@@@@@'
            index = 0
            continue
        index += 1
    stacks = temp_file.split('@@@@@')
    stacks = stacks[0:len(stacks)-1]
    
    for stack in stacks:
        first, second, third = stringStack(stack)
        match = findMatch(first, second, third)
        if not match:
            continue
        sum += map.get(match)
    return sum

def main():
    """ Main program """
    result = partOne()
    print(result)
    result = partTwo()
    print(result)
    
if __name__ == "__main__":
    main()