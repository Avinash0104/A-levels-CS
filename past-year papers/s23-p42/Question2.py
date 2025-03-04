class SaleData():
	# self.ID : string
	# self.Quantity : integer
	def __init__(self, pID, pQuantity):
		self.ID = pID
		self.Quantity = pQuantity

# CircularQueue[5] : SaleData
# Head : integer
# Tail : integer
# NumberOfItems: integer
# MaxSize : integer
CircularQueue = [SaleData("", -1) for i in range(0, 5)]
Head = 0
Tail = 0
NumberOfItems = 0
MaxSize = 5

def Enqueue(item):
	global CircularQueue, Head, Tail, NumberOfItems, MaxSize
	if NumberOfItems >= MaxSize:
		return -1
	else:
		if Tail >= MaxSize -1:
			Tail = 0
		else:
			Tail = Tail + 1
		CircularQueue[Tail] = item
		NumberOfItems = NumberOfItems + 1
		return 1

def Dequeue():
	global CircularQueue, Head, Tail, NumberOfItems, MaxSize
	if NumberOfItems <= 0:
		return None
	else:
		if Head >= MaxSize -1:
			item = CircularQueue[Head]
			Head = 0
		else:
			item = CircularQueue[Head]
			Head = Head + 1
		NumberOfItems = NumberOfItems - 1
		return item

def EnterRecord(id, quantity):
	item = SaleData(id, quantity)
	result = Enqueue(item)
	if result == 1:
		print("Stored")
	else:
		print("Full")

EnterRecord("ADF", 10)
EnterRecord("OOP", 1)
EnterRecord("BXW", 5)
EnterRecord("XXZ", 22)
EnterRecord("HQR", 6)
EnterRecord("LLP", 3)
value = Dequeue()
if value == None:
	print("circular queue is empty")
else:
	print(value.ID, value.Quantity)
EnterRecord("LLP", 3)
print("\n")
for record in CircularQueue:
	print(record.ID, record.Quantity)


	

