import FgameRelevance, Fvalidation

# This will store totalScore of players.
playerData = {} 
# Prebuild of what players can choose to play
maxScores = {1: 301, 2: 501, 3: 701, 4: 901, 5: 999, 6: "Custom"}

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

# Ask for user response
chosenGame = input("Make your choice: (pick a number) ") 
# Convert response to integer
chosenGame = Fvalidation.toInt(chosenGame) 
# Use prebuild dictionary (maxScores) to pick game
chosenGame = FgameRelevance.CheckChosenAmount(chosenGame, maxScores) 

# Pick amount if selection is '6'
if chosenGame == "Custom": 
    # Ask for user response
    chosenGame = input("Enter the desired amount: ") 
    # Convert response to integer
    chosenGame = Fvalidation.toInt(chosenGame) 

print()
print(f'You choose for {chosenGame}')
print()

# Ask for user response
amountOfPlayers = input("How many players will be playing? ") 
# Convert response to int
amountOfPlayers = Fvalidation.toInt(amountOfPlayers) 
# Check if there are more then 0 players
amountOfPlayers = Fvalidation.validateAboveZero(amountOfPlayers) 


print()


i = 1
# Loop for the exact amount of players
for player in range(amountOfPlayers): 
    # Give each player a name
    player = input(f'What is the name of player {i}? ') 
    # Insert every playername into dict with picked game as their value
    playerData.update({player: chosenGame}) 
    print()
    i += 1


print()
print("-"*30)
print("Good Luck and let's play!")
print("Enter the thrown amount per dart.")
print("If thrown into double or triple, enter 'd' (double) or 't' (triple). After that, the game will ask you to enter a score again. You will then enter the normal score and it will double or triple it for you.")
print("all scores will be automatically displayed every round")
print("-"*30)
print()

r = 1 # Round
p = 1 # player

# Used for storing all 3 throws per player
tempScoreList = [] 

# Used later on for storing all scores from the entire match
dataDict = {} 

# Use loop to keep going as long as nobody wins
while True: 
    print()
    print(f'Round {r}')
    print("-"*10)

    # Loop a round for every player and get their key/value after loop go back to the while loop
    for player, score in playerData.items(): 
        print(f"It is now {player}'s turn")
        print(f'your score is {score}')
        print()
        # throw amount (resest after players have thrown 3 times)
        t = 1 

        # Make the player throw 3 times
        for x in range(3): 
            throw = input(f'attempt {t}: ')
            
            # check for double
            if throw == 'd': 
                # Enter score that should be doubled
                throw = int(input("Enter score that will be doubled: ")) 
                 # Double entered score
                throw = FgameRelevance.doubleScore(throw)
                # Add total score to list
                tempScoreList.append(throw) 

            # Check for triple
            elif throw == 't':
                # Enter score that should be tripled
                throw = int(input("Enter score that will be tripled: ")) 
                # Triple entered score
                throw = FgameRelevance.tripleScore(throw) 
                # Add total score to list
                tempScoreList.append(throw) 

            else:
                # Convert score to int
                throw = Fvalidation.toInt(throw) 
                # Add total score to list
                tempScoreList.append(throw) 

            # Displays at which throw the players at
            t += 1 

        print()

        # Make total score of last 3 attempts and put them into a variable
        totalScore = sum(tempScoreList) 

        # update the the dictionary that holds the total score per player and subtract the thrown amount of what they have to throw in total if they do not go below 0
        if playerData[player] - totalScore > 0: 
            playerData[player] = score - totalScore 

        # Check if a player has won the game end then the game
        elif playerData[player] - totalScore == 0: 
            playerData[player] = score - totalScore
            print("*"*60)
            print(f'Player {player} won the game! Congrats!')
            print(f'See you next match!')
            print("*"*60)
            exit()

        # If player goes below 0 then ignore the current round for that player
        elif playerData[player] - totalScore < 0: 
            print("*"*60)
            print("Oh no! This round did not count for you because your score is to high.")
            print("Try again next round")
            print("*"*60)

        # Clear list after 3 turns for next player
        tempScoreList.clear() 
       
        # Create a new dictionary that scores all totalscores per round per player
        # If the round is already in the dictionary just add the new data as an extra dict into the data dict instead of updating the old data
        if r in dataDict: 
            dataDict[r].update({player : totalScore})

        # If the round is not already in the data dict just add them with the current player and their total score
        else: 
            dataDict[r] = {player : totalScore} 

    # Print all scores from previous rounds
    print()
    print('Here are the current scores')
    print("="*30)
    for key, value in dataDict.items():
        print('round' , key , value) 

    print()

    # After everyone has done their attempt go to the next round
    r += 1 
