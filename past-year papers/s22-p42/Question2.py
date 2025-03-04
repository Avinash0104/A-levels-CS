import random
# array[10][10] : integer
array = [[0 for i in range(0, 10)] for j in range(0, 10)]
for row in range(0, 10):
    for col in range(0, 10):
        item = random.randint(0, 100)
        array[row][col] = item

def BubbleSort():
    length = 10
    for x in range(0, length):
        for y in range(0, length - 1):
            for z in range(0, length - y - 1):
                if array[x][z] > array[x][z + 1]:
                    temp = array[x][z]
                    array[x][z] = array[x][z + 1]
                    array[x][z + 1] = temp

def output():
    for a in range(0, 10):
        for b in range(0, 10):
            print(array[a][b], end=" ")
        print('\n')

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = int((Lower + Upper) / 2)
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            if SearchArray[0][Mid] < SearchValue:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1

output()
BubbleSort()
print("----------------------------------")
output()
value1 = BinarySearch(array, 0, 10, array[0][3])
value2 = BinarySearch(array, 0, 10, 13)
print(value1, value2)