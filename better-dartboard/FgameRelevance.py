def CheckChosenAmount(chosenGame:int, maxScores:dict):
    if chosenGame >= 1 and chosenGame <= 6:
        return maxScores[chosenGame]
    else:
        return False


def doubleScore(x):
    x = x * 2
    return x


def tripleScore(x):
    x = x * 3
    return x