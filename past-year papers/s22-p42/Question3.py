class Card():
    # __number: integer
    # __colour: string
    def __init__(self, pNumber, pColour):
        self.__number = pNumber
        self.__colour = pColour
    def GetNumber(self):
        return self.__number
    def GetColour(self):
        return self.__colour

CardArray = [Card(0, " ") for i in range(0, 30)]

try:
    file = open("CardValues.txt", "r")
    count = 1
    for line in file:
        if count % 2 == 1:
            number = int(line)
        if count % 2 == 0:
            colour = str(line).rstrip()
            Cardx = Card(number, colour)
            CardArray[int(count/2) - 1] = Cardx
        count = count + 1
except IOError:
    print("file is not found")

Unavailable = []
Player1 = [Card(0, " ") for i in range(0, 4)]

def ChooseCard():
    CardNumber = 0
    global Unavailable
    while not (CardNumber >= 1 and CardNumber <= 30):
        CardNumber = int(input("Enter an integer to pick a card number: "))
        for index in range(0, len(Unavailable)):
            if CardNumber == Unavailable[index]:
                CardNumber = 0
                print("card in unavailable, choose again")
                break
    Unavailable.append(CardNumber)
    return CardNumber

for x in range(0, 4):
    PlayerNumber = ChooseCard()
    for CardIndex in CardArray:
        if int(CardIndex.GetNumber()) == PlayerNumber:
            Player1[x - 1] = CardIndex
            print(int(CardIndex.GetNumber()))
            print(str(CardIndex.GetColour()))
            break

    

