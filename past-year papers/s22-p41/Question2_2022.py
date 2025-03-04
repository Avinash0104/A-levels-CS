class Balloon():
    # self.__defenceItem string
    # self.__colour string
    # self.__health integer
    def __init__(self, DefenceItemP, ColourP):
        self.__defenceItem = DefenceItemP
        self.__colour = ColourP
        self.__health = 100
    
    def GetDefenceItem(self):
        return self.__defenceItem
    
    def ChangeHealth(self, change):
        self.__health = self.__health + change
        return self.__health
    
    def CheckHealth(self):
        if self.__health < 0:
            return True
        else:
            return False

def Defend(object):
    OppStrength = int(input("Enter the strength of the opponent: "))
    object.ChangeHealth(OppStrength * -1)
    print(object.GetDefenceItem())
    if object.CheckHealth() == False:
        print("balloon has health remaining")
    else:
        print("balloon has no health remaining")
    return object

def main():
    defenceItem1 = str(input("Enter your defence item: "))
    colour1 = str(input("Enter the colour of your balloon: "))
    balloon1 = Balloon(defenceItem1, colour1)
    balloon1 = Defend(balloon1)
        
main()
    
    
