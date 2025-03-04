array = ['' for index in range(0, 10)]
basePointer = 0
frontPointer = 0
rearPointer = -1
queuefull = 10
queueLength = 0 
item = ''

def enq(item):
    global queueLength, queuefull, rearPointer, frontPointer
    if queueLength < queuefull:
        if rearPointer < len(array) - 1:
            rearPointer = rearPointer + 1
        else:
            rearPointer = 1
        queueLength = queueLength + 1
        array[rearPointer] = item
    else:
        print("Queue is full, cannot enqueue")
    
def deq():
    global queueLength, queuefull, rearPointer, frontPointer
    if queueLength == 0:
        item = array[frontPointer]
    else:
        item = array[frontPointer]
        array[frontPointer] = ''
        if frontPointer == len(array) - 1:
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1
        queueLength = queueLength - 1

def dispq():
    print("\n\nCurrent queue elements(s):")
    print(array)
    print("\n")

def main():
    enq('A')
    enq('B')
    dispq()
    enq('C')
    enq('D')
    deq()
    dispq()
    enq('E')
    enq('F')
    enq('G')
    enq('H')
    enq('I')
    enq('J')
    dispq()
    enq('K')
    enq('L')
    dispq()
    deq()
    dispq()
    deq()
    dispq()
    enq('M')
    enq('N')
    enq('O')

main()



    