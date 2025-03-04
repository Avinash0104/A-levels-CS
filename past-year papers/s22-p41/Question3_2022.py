# queue array[0:10] integer
# head integer
# tail integer
# num integer
queue = [0 for i in range(10)]
head = 0
tail = 0
num = 0

def enqueue(queue, head, tail, num, data):
    if num == 10:
        return False, queue, head, tail, num
    queue[tail] = data
    if tail >= 9:
        tail = 0
    else:
        tail = tail + 1
    num = num + 1
    return True, queue, head, tail, num

def dequeue(queue, head, tail, num):
    if num == 0:
        return False, queue, head, tail, num
    data = queue[head]
    if head >= 9:
        head = 0
    else:
        head = head + 1
    num = num - 1
    return data, queue, head, tail, num

def main():
    global queue, head, tail, num
    for index in range(11):
        data = input("enter input data: ")
        result, queue, head, tail, num = enqueue(queue, head, tail, num, data)
        if result == True:
            print("item was added")
        else:
            print("item was not added")
    result2, queue, head, tail, num = dequeue(queue, head, tail, num)
    print(result2)
    result3, queue, head, tail, num = dequeue(queue, head, tail, num)
    print(result3)

main()
