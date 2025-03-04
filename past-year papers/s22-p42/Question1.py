# StackData[10] : integer
# StackPointer : integer
StackData = [0 for i in range (0, 10)]
StackPointer = 0

def output():
    for i in range(0, StackPointer):
        print(StackData[i])
    print("pointer: ", StackPointer)

def Push(item):
    global StackData, StackPointer
    if StackPointer >= 10:
        return False
    else:
        StackData[StackPointer] = item
        StackPointer = StackPointer + 1
        return True

def Pop():
    global StackData, StackPointer
    if StackPointer <= 0:
        return -1
    else:
        StackPointer = StackPointer - 1
        item = StackData[StackPointer]
        return item
        
for ask in range(0, 11):
    number = int(input("enter a number into the stack: "))
    result = Push(number)
    if result == True:
        print("number is added to stack")
    else:
        print("stack is full. Number is not added")
output()
Pop()
Pop()
output()
