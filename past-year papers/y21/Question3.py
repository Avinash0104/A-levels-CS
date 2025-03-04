QueueData = [0 for i in range(20)]
StartPointer = 0
EndPointer = 0
Length = 0
MaxLength = len(QueueData)

StartPointer = StartPointer + 1

def Enqueue(item):
    global QueueData, StartPointer, EndPointer, Length, MaxLength
    if Length < MaxLength:
        if EndPointer == MaxLength:
            EndPointer = 1
        else:
            EndPointer = EndPointer + 1
        QueueData[EndPointer] = item
        Length = Length + 1
        return True
    else:
        return False
    
def Remove():
    global QueueData, StartPointer, EndPointer, Length, MaxLength
    if Length < 2:
        return "No Items"
    else:
        item1 = QueueData[StartPointer]
        item2 = QueueData[StartPointer + 1]
        StartPointer = StartPointer + 2
        return item1, item2

def ReadFile():
    FileName = str(input("Enter a file name: "))
    try:
        File = open(FileName, "r")
        for line in File:
            result = Enqueue(line)
            if result == False:
                return 2
        return 1
    except IOError:
        return -1

ans = ReadFile()
if ans == -1:
    print("file cannot be opened")
if ans == 1:
    print("all items from the file are saved on the queue")
if ans == 2:
    print("not all items from the file are saved on the queue as the queue is full")
print(Remove())
        

    


