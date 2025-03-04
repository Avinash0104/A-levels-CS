# DataArray[100] : integer
DataArray = [0 for i in range(0, 100)]

def ReadFile():
    try:
        file = open("IntegerData.txt", "r")
        count = 0
        for line in file:
            DataArray[count] = int(line)
            count = count + 1
    except IOError:
        print("file cannot be opened")

def FindValues():
    number = 0
    while not (number >= 1 and number <= 100):
        number = int(input("Enter a number to be searched: "))
    count = 0
    for index in range(0, 100):
        if number == DataArray[index]:
            count = count + 1
    return count

def BubbleSort():
    swap = True
    turns = 0
    while swap == True and turns < len(DataArray):
        swap = False
        for x in range(0, len(DataArray) - 1):
            if DataArray[x] > DataArray[x + 1]:
                temp = DataArray[x]
                DataArray[x] = DataArray[x + 1]
                DataArray[x + 1] = temp
                swap = True
        turns = turns + 1
    for item in DataArray:
        print(item)

ReadFile()
result = FindValues()
print("the number appears", result, "times")
BubbleSort()