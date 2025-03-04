class Card():
    # number : integer
    # colour : string
    def __init__(self, pNumber, pColour):
        self.__number = pNumber
        self.__colour = pColour
    def GetNumber(self):
        return self.__number
    def GetColour(self):
        return self.__colour

class Hand():
    # CardArray: Card
    def __init__(self, card1, card2, card3, card4, card5):
        self.__Cards = [card1, card3, card3, card4, card5]
        self.__FirstCard = 0
        self.__NumberCards = 5
    def GetCard(self, index):
        return self.__Cards[index]

def CalculateValue(PlayerHand):
    total = 0
    for x in range(0, 5):
        item = PlayerHand.GetCard(x)
        if item.GetColour() == "red":
            total = total + 5
        if item.GetColour() == "blue":
            total = total + 10
        if item.GetColour() == "yellow":
            total = total + 15
        total = total + item.GetNumber()
    return total
    
CardArray = [Card(0, " ") for index in range(0, 15)]
for i in range(0, 5):
    CardX = Card(i, "red")
    CardArray[i] = CardX
for j in range(0, 5):
    CardY = Card(j, "blue")
    CardArray[j + 5] = CardY
for k in range(0, 5):
    CardZ = Card(k, "yellow")
    CardArray[k + 10] = CardZ

Player1 = Hand(Card(1, "red"), Card(2, "red"), Card(3, "red"), Card(4, "red"), Card(1, "yellow"))
Player2 = Hand(Card(2, "yellow"), Card(3, "yellow"), Card(4, "yellow"), Card(5, "yellow"), Card(1, "blue"))

score1 = CalculateValue(Player1)
score2 = CalculateValue(Player2)
if score1 > score2:
    print("Player 1 wins")
elif score1 < score2:
    print("Player 2 wins")
else:
    print("it is a draw")



