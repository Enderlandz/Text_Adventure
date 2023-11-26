def IsConvertibleToInt(number):
    for digit in number:
        if not digit.isdigit():
            return False
    return True

def getChoiceFromPlayer():
    playerChoice = input("> ")
    while not IsConvertibleToInt(playerChoice):
        print("C'mon, just play along")
        playerChoice = input('Please input a valid playerChoice\n> ')
    return int(playerChoice)

def getValidInput():
    playerChoice = getChoiceFromPlayer()
    while playerChoice > 2:
        print("That's higher than 2, no can do")
        playerChoice = getChoiceFromPlayer()
    while playerChoice < 1:
        print('Lower than 1, nuh uh')
        playerChoice = getChoiceFromPlayer()
    return playerChoice
