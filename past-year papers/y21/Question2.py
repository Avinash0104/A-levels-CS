class HiddenBox():
    # __BoxName : string
    # __Creator : string
    # __DateHidden : date
    # __GameLocation : string
    # __LastFinds[10][2] : string
    # __Active : boolean
    def __init__(self, pBoxName, pCreator, pDateHidden, pGameLocation):
        self.__BoxName = pBoxName
        self.__Creator = pCreator
        self.__DateHidden = pDateHidden
        self.__GameLocation = pGameLocation
        self.__LastFinds = [["" for i in range(0, 2)] for j in range(0, 10)]
        self.__Active = False

    def GetBoxName(self):
        return self.__BoxName
    
    def GetGameLocation(self):
        return self.__GameLocation

def NewBoxes():
    global TheBoxes
    newName = str(input("Enter name of box: "))
    newCreator = str(input("Enter your username: "))
    newDateHidden = input("Enter date box was hidden")
    newGameLocation = input("Enter location of the box")
    NewBox = HiddenBox(newName, newCreator, newDateHidden, newGameLocation)
    TheBoxes.append(NewBox)

class PuzzleBox(HiddenBox):
    # __PuzzleText : string
    # __Solution : string
    def __init__(self, pBoxName, pCreator, pDateHidden, pGameLocation, pPuzzleText, pSolution):
        HiddenBox.__init__(self, pBoxName, pCreator, pDateHidden, pGameLocation)
        self.__PuzzleText = pPuzzleText
        self.__Solution = pSolution


# TheBoxes : HiddenBox
TheBoxes = [HiddenBox("", "", "", "") for m in range(10000)]

NewBoxes()
