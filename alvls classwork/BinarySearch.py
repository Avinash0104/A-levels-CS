numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
upperBound = len(numbers) - 1
lowerBound = 0
found = False
notfound = False
num = int(input("number to be found between 0 to 9: "))
while num < lowerBound and num > upperBound:
    num = int(input("number to be found between 0 to 9: "))
while found != True or upperBound > lowerBound:
    mid = int(((upperBound - lowerBound) / 2))
    if num > mid:
        lowerBound = mid + 1
    elif num < mid:
        upperBound = mid - 1
    elif num == mid:
        found = True

    