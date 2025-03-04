class Picture():
    # __Description : string
    # __Width : integer
    # __Height : integer
    # __FrameColour : string
    def __init__(self, pDescription, pWidth, pHeight, pFrameColour):
        self.__Description = pDescription
        self.__Width = pWidth
        self.__Height = pHeight
        self.__FrameColour = pFrameColour
    def GetDescription(self):
        return self.__Description
    def GetWidth(self):
        return self.__Width
    def GetHeight(self):
        return self.__Height
    def GetFrameColour(self):
        return self.__FrameColour
    def SetDescription(self, newDescription):
        self.__Description = newDescription

PictureArray = [Picture("", 0, 0, "") for i in range(0, 100)]

def ReadData():
    try:
        file = open("Pictures.txt", "r")
        count = 0
        pos = 0
        for line in file:
            if count % 4 == 0:
                newDescription = str(line).rstrip()
            if count % 4 == 1:
                newWidth = int(line)
            if count % 4 == 2:
                newHeight = int(line)
            if count % 4 == 3:
                newFrameColour = str(line).rstrip().lower()
                PictureArray[pos] = Picture(newDescription, newWidth, newHeight, newFrameColour)
                pos = pos + 1
            count = count + 1
        file.close()
    except IOError:
        print("file cannot be found")

ReadData()
userFrameColour = str(input("enter the frame colour: ")).lower()
userMaxWidth = int(input("enter the max width: "))
userMaxHeight = int(input("enter the max height: "))
for item in PictureArray:
    description = str(item.GetDescription())
    width = int(item.GetWidth())
    height = int(item.GetHeight())
    FrameColour = str(item.GetFrameColour())
    if (height <= userMaxHeight) and (width <= userMaxWidth) and (FrameColour == userFrameColour):
        print(description)
        print(width)
        print(height)
        print(FrameColour)
        print(" ")


    
