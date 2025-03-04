# players array[0:11] string
# scores array[0:11] integer
players = []
scores = []

def ReadHighScores():
    global players, scores
    try:
        file = open("HighScore.txt", 'r')
        index = 0
        for item in file:
            if index % 2 == 1:
                scores.append(int(item))
            else:
                players.append(str(item))
            index = index + 1
        file.close()
    except IOError:
        print("File is not found")

def OutputHighScores():
    global players, scores
    for count in range(10):
        print(players[count], scores[count])

def UpdateHighScores(NewPlayer, NewScore):
    global players, scores
    if NewScore > scores[9]:
        index = 0
        written = False
        while written == False:
            if NewScore > scores[index]:
                lim = 9
                while lim > index:
                    scores[lim] = scores[lim - 1]
                    players[lim] = players[lim - 1]
                    lim = lim - 1
                scores[lim] = NewScore
                players[lim] = NewPlayer + "\n"
                written = True
            index = index + 1
    return players, scores
    

def main():
    global players, scores
    ReadHighScores()
    OutputHighScores()
    PlayerName = ""
    PlayerScore = 0
    while len(PlayerName) != 3:
        PlayerName = str(input("Enter a 3-character player name: "))
    while int(PlayerScore) < 1 or int(PlayerScore) > 100000:
        PlayerScore = int(input("Enter player's score between 1 and 100000: "))
    players, scores = UpdateHighScores(str(PlayerName), int(PlayerScore))
    OutputHighScores()
    WriteTopTen()

def WriteTopTen():
    global players, scores
    newfile = open("NewHighScore.txt", 'w')
    index = 0
    while index < 10:
        newfile.write(players[index])
        newfile.write(str(scores[index]) + "\n")
        index = index + 1

main()

        