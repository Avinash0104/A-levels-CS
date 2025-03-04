# Queue[100] : integer
# HeadPointer : integer
# TailPointer : integer
Queue = [0 for i in range(0, 100)]
HeadPointer = -1
TailPointer = -1
Length = 0
MaxSize = len(Queue)

def Enqueue(item):
	global Queue, HeadPointer, TailPointer, Length
	if Length >= MaxSize:
		return False
	else:
		HeadPointer = HeadPointer + 1
		Queue[HeadPointer] = item
		Length = Length + 1
		return True

for i in range(1, 21):
	result = Enqueue(i)
	if result == True:
		print("Successful")
	else:
		print("Unsuccessful")

def RecursiveOutput(count):
	global HeadPointer, TailPointer, Queue, Length
	if count == HeadPointer:
		total = 0
	if count != TailPointer:
		return (Queue[count] + RecursiveOutput(count - 1))
	else:
		return 0

print(RecursiveOutput())
	
