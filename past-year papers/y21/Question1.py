TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def InsertionSort(array):
    for count in range(len(array)):
        DataToInsert = TheData[count]
        Inserted = 0
        NextValue = count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1

def output(array):
    for count in range(len(array)):
        print(array[count])

def LinearSearch(array):
    num = int(input("Enter a whole number: "))
    found = False
    count = 0
    while count < len(array) and found == False:
        if num == array[count]:
            found = True
        count = count + 1
        
    if found == True:
        print("found")
    else:
        print("not found")
    return found


print("data before sorting")
output(TheData)

InsertionSort(TheData)

print("data after sorting")
output(TheData)

LinearSearch(TheData)