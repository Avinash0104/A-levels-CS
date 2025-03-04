Animal = [] # 20 elements
Colour = [] # 10 elements
# AnimalTopPointer integer
# ColourTopPointer integer
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global Animal, AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer = AnimalTopPointer + 1
        return True

def PopAnimal():
    global Animal, AnimalTopPointer
    # ReturnData string
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData

def ReadData():
    global Animal, Colour
    global AnimalTopPointer, ColourTopPointer

    try:
        AnimalFile = open("AnimalData.txt", 'r')
        for item in AnimalFile:
            PushAnimal(item)
        AnimalFile.close()
    except IOError:
        print("could not find file")
    
    try:
        ColourFile = open("ColourData.txt", 'r')
        for item in ColourFile:
            PushColour(item)
        ColourFile.close()
    except IOError:
        print("could not find file")

def PushColour(DataToPush):
    global Colour, ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopColour():
    global Colour, ColourTopPointer
    # ReturnData string
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return ReturnData

def OutputItem():
    animal = PopAnimal()
    colour = PopColour()
    if colour == "":
        print("no colour.")
        PushColour(colour)
    if animal == "":
        print("no animal.")
        PushAnimal(animal)
    else:
        print(colour, animal)

def main():
    ReadData()
    for i in range(0, 4):
        OutputItem()

main()




