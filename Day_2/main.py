
map = {
    "rock": 1,
    "paper": 2,
    "scissor": 3
}

def rockPaperScissor(player, enemy):
    sum = map.get(player) 
    if player == enemy:
        return sum + 3
    if player == "rock":
        if enemy == "paper":
            return sum
        if enemy == "scissor":
            return sum + 6
    if player == "paper":
        if enemy == "rock":
            return sum + 6
        if enemy == "scissor":
            return sum
    if player == "scissor":
        if enemy == "paper":
            return sum + 6
        if enemy == "rock":
            return sum
    return sum

def rockPaperScissorAdvanced(player, enemy):
    # Loose
    if player == "rock":
        if enemy == "rock":
            return 3
        if enemy == "paper":
            return 1
        if enemy == "scissor":
            return 2
    # Draw
    if player == "paper":
        return map.get(enemy) + 3
    # Win
    if player == "scissor":
        if enemy == "rock":
            return 2 + 6
        if enemy == "paper":
            return 3 + 6
        if enemy == "scissor":
            return 1 + 6

def convertInput(content):
    data = content.replace("A", "rock")
    data = data.replace("B", "paper")
    data = data.replace("C", "scissor")
    
    data = data.replace("Y", "paper")
    data = data.replace("X", "rock")
    data = data.replace("Z", "scissor")
    return data

def partOne():
    file1 = open('./input.txt', 'r')
    lines = file1.readlines()
    sum = 0
    for line in lines:
        line = convertInput(str(line)).strip()
        choices = line.split()
        sum += int(rockPaperScissor(choices[1], choices[0]))
    return sum

def partTwo():
    file1 = open('./input.txt', 'r')
    lines = file1.readlines()
    sum = 0
    for line in lines:
        line = convertInput(str(line)).strip()
        choices = line.split()
        sum += int(rockPaperScissorAdvanced(choices[1], choices[0]))
    return sum

def main():
    """ Main program """
    result = partOne()
    print(result)
    result = partTwo()
    print(result)
    
if __name__ == "__main__":
    main()
    