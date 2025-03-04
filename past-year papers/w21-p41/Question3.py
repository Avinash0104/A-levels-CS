# RootPointer : integer
# FreeNode : integer
# ArrayNodes[20][3] : integer
RootPointer = -1
FreeNode = 0
ArrayNodes = [[0 for i in range(0, 3)] for j in range(0, 20)]

def AddNodes():
    global RootPointer, FreeNode, ArrayNodes
    NodeData = int(input("Enter the data: "))
    if FreeNode < 20:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")

def InOrder(RootPointer):
    if ArrayNodes[RootPointer][0] != -1:
        InOrder(ArrayNodes[RootPointer][0])
    print(str(ArrayNodes[RootPointer][1]))
    if ArrayNodes[RootPointer][2] != -1:
        InOrder(ArrayNodes[RootPointer][2])

def PrintAll(ArrayNodes):
    for j in range(0, 10):
        print(str(ArrayNodes[j][0]) + " " + str(ArrayNodes[j][1]) + " " + str(ArrayNodes[j][2]))

for item in range(10):
    AddNodes()
PrintAll(ArrayNodes)
InOrder(0)