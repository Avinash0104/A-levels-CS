start = -1
heapPointer = 0
nullPoint = -1

linkedlist = [34, 44, 6, 12, None, None, None, None, None, None]
linkedlistPointers = [(i + 1) for i in range(10)]
linkedlistPointers[9] = -1

# add new data
def add(item):
    global start, heapPointer
    if heapPointer == nullPoint:
        print("linked list is full")
    else:
        temp = start
        start = heapPointer
        heapPointer = linkedlistPointers[heapPointer]
        linkedlist[start] = item
        linkedlistPointers[start] = temp
        print("New data ", item, "added to linked list")

# delete data
def delete(item):
    global start, heapPointer
    if start == nullPoint:
        print("Linked list is empty")
    else:
        index = start
        while linkedlist[index] != item and index != nullPoint:
            oldindex = index
            index = linkedlistPointers[index]
        if index == nullPoint:
            print("Data", item, "not found")
        else:
            linkedlist[index] = None
            temp = linkedlistPointers[index]
            linkedlistPointers[index] = heapPointer
            heapPointer = index
            linkedlistPointers[oldindex] = temp
            print("data", item, "deleted successfully")

def main():
    print(linkedlist)
    add(33)
    add(78)
    delete(6)
    delete(99)
    print(linkedlist)

main()