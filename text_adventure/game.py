from text_adventure.inputHandling import getValidInput

def entry():
    gameBeaten = False
    gameOver = False
    deeper = False
    outside = False
    print('Oh my! Welcome, come on in! Make yourself comfortable.')
    print('Welcome to my small text adventure! This is the second game I ever make, and this time I am alone (mostly).')
    print("But I'm babbling too much, let's not delay this any further.")
    print('Well then,')
    name = input('What shall your name be?\n> ')
    print('Welcome, {}, and good luck'.format(name))

    print('You find yourself inside a cave\nWhat do you do?\n[1] Go deeper into the cave\n[2] Try to leave the cave')
    playerChoice = getValidInput()
    if playerChoice == 1:
        print('You go deeper into the cave')
        deeper = True
    if playerChoice == 2:
        print('You try to find a way outside')
        outside = True
    
    if deeper == True:
        print('You come across a sleeping giant bat!\nWhat do you do?\n[1] Sneak past the bat\n[2] Try to find something to throw at the bat')
        playerBatChoice = getValidInput()
        if playerBatChoice == 1:
            print('As you attempt to sneak past the bat, you step on a branch, waking the bat.')
            gameOver = True
        if playerBatChoice == 2:
            print('You find a rock nearby, where do you aim it at?\n[1] The head of the bat\n[2] The torso of the bat')
            playerRockChoice = getValidInput()
            if playerRockChoice == 1:
                print('The bat wakes up in confusion, but the damage to its ears stuns it!')
                print('You manage to sprint by the bat while it is stunend')
                print('You go deeper into the caves...')
                gameBeaten = True
            if playerRockChoice == 2:
                print('The bat wakes up, shrugging off the hit')
                gameOver = True
    
    if outside == True:
        print('As you try to find the exit of the cave, you encounter a boulder that blocks your path.')
        print('What do you do?\n[1] Try to climb the boulder\n[2] Try to find a way around the boulder')
        playerBoulderChoice = getValidInput()
        if playerBoulderChoice == 1:
            print('You prepare yourself, and soon after you start climbing the boulder')
            print('Before you reach the top of the boulder, however, you see a giant spider standing in the way!')
            print('What do you do?\n[1] Keep climbing, ignoring the spider\n[2] Try to scare the spider away')
            playerSpiderChoice = getValidInput()
            if playerSpiderChoice == 1:
                print("The spider is stunned by how much you don't give a fuck about it, and moves away from your path, instinctively")
                print('You find the exit of the cave...')
                gameBeaten = True
            if playerSpiderChoice == 2:
                print('The spider laughs at your pathetic attempt, and rushes toward you')
                gameOver = True

        if playerBoulderChoice == 2:
            print('Trying to find a way around, you go deeper into a dark room, and eventually slip on some moss, hitting your head')
            gameOver = True

    if gameOver == True:
        print('Game Over!')
        exit(0)
    
    if gameBeaten == True:
        print('You finished the game!')
        exit(0)

    exit(0) 