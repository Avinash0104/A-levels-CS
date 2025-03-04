# Declare an array "queue" of data type string
Queue = ['', '', '', '', '', '', '', '', '', '']
# Declare QueueHeadPointer as an integer
QueueHeadPointer = 0
# Declare QueueTailPointer as an integer
QueueTailPointer = 0
# Declare QueueTailPointer as an integer
NumberOfItems = 0

def Enqueue(Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems, DataToAdd):
    if NumberOfItems == 10:
        return False, Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems
    Queue[QueueTailPointer] = DataToAdd
    if QueueTailPointer >= 9:
        QueueTailPointer = 0
    else:
        QueueTailPointer = QueueTailPointer + 1
    NumberOfItems = NumberOfItems + 1
    return True, Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems

def Dequeue(Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems):
    if NumberOfItems == 0:
        return False, Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems
    DataToRemove = Queue[QueueHeadPointer]
    QueueHeadPointer = QueueHeadPointer + 1
    if QueueHeadPointer >= 9:
        QueueHeadPointer = 0
    NumberOfItems = NumberOfItems - 1
    return DataToRemove, Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems

def main():
    global Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems
    for i in range(11):
        item = str(input("Enter a data item: "))
        value, Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems = Enqueue(Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems, item)
        if value == True:
            print("Successful")
        else:
            print("Unsuccessful")
    
    value, Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems = Dequeue(Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems)
    print(value)
    value, Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems = Dequeue(Queue, QueueHeadPointer, QueueTailPointer, NumberOfItems)
    print(value)

main()
    


    