class Card():
    name = "Avinash"
    def __init__(self):
        self.__number = 0
        self.__colour = ""
    def SetNumber(self, num):
        self.__number = num
    def SetColour(self, paint):
        self.__colour = paint

Card1 = Card()
Card1.SetColour("green")
Card1.SetNumber(9)
print(Card1.name)