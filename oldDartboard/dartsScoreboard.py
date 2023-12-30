# Function to see if someone won
def CheckForWin(i: int, throw: int, totalScore: list):

    tempScore = totalScore.pop(i)
    checkScore = tempScore - throw
    if checkScore == 0:
        totalScore.insert(i, tempScore)
        return True
    else:
        totalScore.insert(i, tempScore)
        return False


# Function to set someones score to zero in the list of totalScores
def SetScoreToZero(i: int, totalScore: list):

    tempScore = totalScore.pop(i)
    newScore = tempScore - tempScore
    totalScore.insert(i, newScore)


# Funtion to display leaderboard after some has won the game
def ShowWinner(currentPlayer: str, playersNames: list, totalScore: list):

    print(f"\n\r{currentPlayer} won the game!")
    print("="*30)
    j = 0
    # Shows every player's score except for the winner
    for player in playersNames:
        if totalScore[j] != 0:
            print(f"{player} had a score of {totalScore[j]}")
            print("-"*10)
        j += 1

totalScore = [] # Stores the total score players have to reach for every player individually
playersNames = [] # Stores all names of every player that enters the game
pickGame = 1 # The default gamemode (Changed later on)
currentPlayer = "" 

print()
# Set the gamemode
while True:
    pickGame = input("What game will you be playing? (Enter a number): ")
    try:
        pickGame = int(pickGame)
        if pickGame <= 0:
            print("You can't start a game where you have to get 0 points or less. Try again.")
        else:
            break
    except:
        print("Please enter a valid number\n\r")

print()
print(f'The game is set to {pickGame}. Players will now need to throw {pickGame} to win.')
print()
# Set the amount of players
while True:
    playerCount = input("How many players will play this round?: ")
    if playerCount <= "0":
        print("You can't play with 0 players! You need to enter at least 1 player\n\r")
    else:
        try:
            playerCount = int(playerCount)
            break
        except:
            print("Please enter a valid number\n\r")

# Preparing everything after given amount of players
for player in range(playerCount): # For the given amount of players loop the following code:
    totalScore.append(pickGame) # Set totalScore
    
    playerName = input("Enter the player's name: ").capitalize()
    print()
    playersNames.append(playerName) # Enter given players names into list

print("\n\rPlay")
print("*"*60)



i = 0 # Set counter to the first player (the counter is used for iterating over the list of total scores and entered players. The position in those lists will always correspond to the right players.)
throws = False
end = False
# Playing the game
while True:
    for currentPlayer in playersNames:
        # Show the current total score of the current player before throwing.
        print(f"{currentPlayer} has to throw {totalScore[i]} to win this game!")
        
        # Ask points for every throw and see if it's valid
        while True:
            throw1 = input(f"How much was the first throw for {currentPlayer}?: ")
            try:
                # Convert the input to an integer (otherwise the number is seen as a string)
                if throw1 < 0:
                    print(f"You can't enter a score lower than 0")
                elif throw1 == "d" or throw1 == "D":
                    throw1 = throw1 * 2
                elif throw1 == "t" or throw1 == "T":
                    throw1 = throw1 * 3
                else:
                    # Check if player won with the current throw
                    checkWin = CheckForWin(i, throw1, totalScore)
                    if checkWin == True:
                        # This function sets the score of currentplayer to zero so he doesn't pop up in the list of players who still have points
                        SetScoreToZero(i, totalScore)

                        #The function shows the players the leaderboard when someone has won
                        ShowWinner(currentPlayer, playersNames, totalScore)

                        # Use this so you break out of the 'while' loop before exiting the program (otherwise it crashes)
                        end = True
                        break
                    else:
                        break
            except:
                print("You didn't enter a valid throw \n\r")

        if end == True:
            exit()


        while True:
            throw2 = input(f"How much was the second throw for {currentPlayer}?: ")
            try:
                throw2 = int(throw2)
                if throw2 < 0:
                    print(f"You can't enter a score lower than 0")
                elif throw2 >= 21:
                    print(f"You can't enter a score higher than 20")
                else:
                    checkWin = CheckForWin(i, throw2, totalScore)
                    if checkWin == True:
                        SetScoreToZero(i, totalScore)
                        ShowWinner(currentPlayer, playersNames, totalScore)
                        end = True
                        break
                    else:
                        break
            except:
                print("You didn't enter a valid throw \n\r")

        if end == True:
            exit()

        # Third throw doesn't need an early check because that's already being done by the remaining code
        while True:
            throw3 = input(f"How much was the third throw for {currentPlayer}?: ")
            try:
                throw3 = int(throw3)
                if throw3 < 0:
                    print(f"You can't enter a score lower than 0")
                elif throw3 >= 21:
                    print(f"You can't enter a score higher than 20")
                else:
                    break
            except:
                print("You didn't enter a valid throw \n\r")
                

        # Calculate total score of current round and show it to player(s)
        score = throw1 + throw2 + throw3
        print(f"\n\rThe total score is {score} \n\r")


        # Pick the total score out of the list at the right index. Retract the thrown score from it and put it bag in the list on the same index
        tempScore = totalScore.pop(i)
        newScore = tempScore - score
        # If player threw too much, put back the old score and proceed to following code
        if newScore < 0:
            totalScore.insert(i, tempScore)
            print(f"\n\r{currentPlayer} has thrown too many points and therefore this round will not count. Try again next turn!\n\r")
        else:
            # If player has not exceeded the limit insert the new earned score into the list of total scores
            totalScore.insert(i, newScore)


        # Check if the current player won the game
        if totalScore[i] == 0:
            ShowWinner(currentPlayer, playersNames, totalScore)
            exit()
            
        # After all inputs are entered and scores are updated, add 1 to the counter to proceed to the next player
        i += 1
        # Reset counter when reached max amount of players (This means every player has played a round)
        if i >= playerCount:
            i = 0
