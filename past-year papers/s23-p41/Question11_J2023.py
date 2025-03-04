DataArray = [] #25 elements
try:
    DataFile = open("yea.txt", 'r')
    for line in DataFile:
        DataArray.append(line)
    DataFile.close()
except IOError:
    print("Could not find file")

def PrintArray():
    # sentence : string
    sentence = ""
    for index in range(len(DataArray)):
        sentence = sentence + str(DataArray[index]) + " "
    print(sentence)

def LinearSearch(intArray, intSearch):
    # count : integer
    count = 0
    for index in range(0, len(intArray)):
        if intSearch == int(intArray[index]):
            count = count + 1
        index = index + 1
    return count


def main():
    PrintArray()
    number = int(input("Please enter a number between 0 and 100: "))
    while number > 100 or number < 0:
        number = int(input("The number is not in the range given. Please enter a number between 0 and 100: "))
    result = LinearSearch(DataArray, number)
    print("the number", number, "is found ", result, " times")


main()
