class Balloon():
    # health as integer
    # colour as string
    # defence item as string
    def __init__(self, input_colour, input_defence_item):
        self.__health = 100
        self.__colour = input_colour
        self.__defenceItem = input_defence_item
    def GetDefenceItem(self):
        return self.__defenceItem
    def ChangeHealth(self, change):
        self.__health = self.__health + change
    def CheckHealth(self):
        if self.__health <= 0:
            return True
        else:
            return False

def defend(input_balloon):
    opp_strength = int(input("Strength of the opponent: "))
    input_balloon.ChangeHealth(opp_strength * -1)
    print("your balloon was defended with the defence item", input_balloon.GetDefenceItem())
    if input_balloon.CheckHealth == True:
        print("Your balloon has no health remaining")
    else:
        print("Your balloon has some remaining health")
    return input_balloon

def main():
    defenceItem1 = str(input("Enter your defence item: "))
    colour1 = str(input("Enter the colour of your balloon: "))
    balloon1 = Balloon(colour1, defenceItem1)
    balloon1 = defend(balloon1)

main()