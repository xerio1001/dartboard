import FgameRelevance, Fvalidation

playerData = {} # This will store totalScore of players.
maxScores = {1: 301, 2: 501, 3: 701, 4: 901, 5: 999, 6: "Custom"}
roundData = {} # Stores data per round

print(f'Select by number what game you will be playing:')
print()
print(f'1: 301 (fast)')
print("-"*15)
print(f'2: 501 (normal)')
print("-"*15)
print(f'3: 701 (somewhat competitive)')
print("-"*15)
print(f'4: 901 (showoff)')
print("-"*15)
print(f'5: 999 (Nah you crazy)')
print("-"*15)
print(f'6: ? (I can decide for myself thank you.)')
print("-"*15)
print()

###########

chosenGame = input("Make your choice: ") # Ask for user response

chosenGame = Fvalidation.toInt(chosenGame) # Convert response to integer
chosenGame = FgameRelevance.CheckChosenAmount(chosenGame, maxScores) # Use prebuild dictionary (maxScores) to pick game

if chosenGame == "Custom": # Pick amount if selection is '6'
    chosenGame = input("Enter the desired amount: ") # Ask for user response
    chosenGame = Fvalidation.toInt(chosenGame) # Convert response to integer

print()
print(f'You choose for {chosenGame}')
print()


amountOfPlayers = input("How many players will be playing? ") # Ask for user response

amountOfPlayers = Fvalidation.toInt(amountOfPlayers) # Convert response to int
amountOfPlayers = Fvalidation.validateAboveZero(amountOfPlayers) # Check if there are more then 0 players

print()

i = 1
for player in range(amountOfPlayers): # Loop for the exact amount of players
    player = input(f'What is the name of player {i}? ') # Give each player a name
    playerData.update({player: chosenGame}) # Insert every playername into dict with picked game as their value
    print()
    i += 1


print()
print("-"*30)
print("Good Luck and let's play!")
print("Enter the thrown amount per dart.")
print("If thrown into double or triple, enter 'd' (double) or 't' (triple). After that, the game will ask you to enter a score again. You will then enter the normal score and it will double or triple it for you.")
print("all scores will be automatically displayed every 5 rounds")
print("-"*30)
print()

r = 1 # Round
p = 1 # player
tempScoreList = []
tempDataDict = {}

while True: # Use loop to keep going as long nobody wins
    print()
    print(f'Round {r}')
    print("-"*10)
    print(roundData)
    if r % 5 == 0:
        print(f'Here are the scores {playerData}')

    for player, score in playerData.items(): # Loop a round for every player and get their key/value after loop go back to the while loop
        print(f"It is now {player}'s turn")
        print(f'your score is {score}')
        print()
        t = 1 # throw amount (resest after players have thrown 3 times)

        for x in range(3): # Make the player throw 3 times
            throw = input(f'attempt {t}: ')
            
            if throw == 'd': # check for double
                throw = int(input("Enter score that will be doubled: ")) # Enter score that should be doubled
                throw = FgameRelevance.doubleScore(throw) # Double entered score
                tempScoreList.append(throw) # Add total score to list

            elif throw == 't':
                throw = int(input("Enter score that will be tripled: ")) # Enter score that should be tripled
                throw = FgameRelevance.tripleScore(throw) # Triple entered score
                tempScoreList.append(throw) # Add total score to list

            else:
                throw = Fvalidation.toInt(throw) # Convert score to int
                tempScoreList.append(throw) # Add total score to list
            t += 1 # Displays at which throw the players at
        print()

        totalScore = sum(tempScoreList) # Make total score of last 3 attempts and put them into a variable
        tempScoreList.clear() # Clear list after 3 turns for next player
        playerData[player] = score - totalScore

        if playerData[player] == 0:
            print("*"*60)
            print(f'Player {player} won the game! Congrats!')
            print(f'See you next match!')
            print("*"*60)
            exit()

    r += 1 # After everyone has done their attempt go to the next round
