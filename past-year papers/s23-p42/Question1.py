# Animals[10] : integer
Animals = ["" for i in range(0, 10)]
Animals[0] = "horse"
Animals[1] = "lion"
Animals[2] = "rabbit"
Animals[3] = "mouse"
Animals[4] = "bird"
Animals[5] = "deer"
Animals[6] = "whale"
Animals[7] = "elephant"
Animals[8] = "kangaroo"
Animals[9] = "tiger"

def SortDescending():
	# ArrayLength : integer
	# Temp : string
	ArrayLength = len(Animals)
	for x in range(0, ArrayLength - 1):
		for y in range(0, ArrayLength - x - 1):
			if Animals[y] < Animals[y + 1]:
				temp = Animals[y]
				Animals[y] = Animals[y + 1]
				Animals[y + 1] = temp

SortDescending()
for i in Animals:
	print(i)