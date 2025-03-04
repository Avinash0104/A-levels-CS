# Jobs[100][2] : integer
# NumberOfJobs : integer
Jobs = [[0 for i in range(0, 2)] for j in range(0, 100)]
NumberOfJobs = None

def Initialise():
	global NumberOfJobs
	NumberOfJobs = 0
	for j in range(0, 100):
		for i in range(0, 2):
			Jobs[j][i] = -1

def AddJob(JobNumber, Priority):
	Added = False
	for j in range(0, 100):
		if Jobs[j][0] == -1:
			Added = True
			Jobs[j][0] = JobNumber
			Jobs[j][1] = Priority
			break
	if Added == True:
		print("Added")
		NumberOfJobs = NumberOfJobs + 1
	else:
		print("Not Added")

def InsertionSort():
	upperbound = len(Jobs) - 1
	lowerbound = 0
	index = lowerbound + 1
	place = 0
	
	while index <= upperbound:
		key = Jobs[index][1]
		place = index - 1
		while place >= lowerbound and Jobs[place][1] > key:
			temp1 = Jobs[place + 1][1]
			temp0 = Jobs[place + 1][0] 
			Jobs[place + 1][1] = Jobs[place][1]
			Jobs[place + 1][0] = Jobs[place][0]
			Jobs[place][1] = temp1
			Jobs[place][0] = temp0
			key = Jobs[place][1]
			place = place - 1
		index = index + 1

def PrintArray():
	for j in range(0, 100):
		if Jobs[j][0] != -1 and Jobs[j][1] != -1:
			print(Jobs[j][0], "priority", Jobs[j][1])

Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)
InsertionSort()
PrintArray()

(78, 'priority', 1)
(33, 'priority', 8)
(526, 'priority', 9)
(12, 'priority', 9)
(12, 'priority', 10)
			
	