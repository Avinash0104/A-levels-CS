class Character():
	# Name : string
	# XCoordinate : integer
	# YCoordinate : integer
	def __init__(self, pName, pX, pY):
		self.__Name = pName
		self.__XCoordinate = pX
		self.__YCoordinate = pY
	def GetName(self):
		return self.__Name
	def GetX(self):
		return self.__XCoordinate
	def GetY(self):
		return self.__YCoordinate
	def ChangePosition(self, XChange, YChange):
		self.__XCoordinate = self.__XCoordinate + XChange
		self.__YCoordinate = self.__YCoordinate + YChange

CharacterArray = []
try:
	file = open("Characters.txt", 'r')
	for j in range(0, 10):
		name = file.readline().rstrip()
		X = file.readline().rstrip()
		Y = file.readline().rstrip()
		TempC = Character(name, int(X), int(Y))
		CharacterArray.append(TempC)
	file.close()
except:
	print("file could not be opened")

Exists = False
while Exists == False:
	CharacterName = str(input("Enter a character's name: "))
	position = 0
	for item in CharacterArray:
		if str(item.GetName().rstrip()) == CharacterName:
			Exists = True
			break
		else:
			position = position + 1

Valid = False
while Valid == False:
	Action = input("Enter a valid move: ")
	if Action.upper() == 'A':
		CharacterArray[position].ChangePosition(-1, 0)
		Valid = True
	elif Action.upper() == 'W':
		CharacterArray[position].ChangePosition(0, 1)
		Valid = True
	elif Action.upper() == 'S':
		CharacterArray[position].ChangePosition(0, -1)
		Valid = True
	elif Action.upper() == 'D':
		CharacterArray[position].ChangePosition(1, 0)
		Valid = True

print(str(CharacterArray[position].GetName), "has changed its position to X = " + str(CharacterArray[position].GetX) + " and Y = " + str(CharacterArray[position].GetY))
	
	









	