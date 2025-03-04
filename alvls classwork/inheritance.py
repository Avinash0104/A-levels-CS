class student():
    def __init__(self, in_name, in_dob, in_exam_mark):
        self.__name = in_name
        self.__dob = in_dob
        self.__exam_mark = in_exam_mark
    def displayExamMark(self):
        print("Name: ", self.__name)
        print("Exam Mark: ", self.__exam_mark)

class fullTimeStudent(student):
    def __init__(self, name, dob, creditHours):
        student.__init__(self, name, dob)
        self.__credits = creditHours
    def displayCreditHours(self):
        print("Name: ", self.__name)
        print("Credit Hours:  ", self.__credits)

    
class partTimeStudent(student):
    def __init__(self, name, dob, SpendingTime):
        student.__init__(self, name, dob)
        self.__spending = SpendingTime
    def displaySpendingTime(self):
        print("Name: ", self.__name)
        print("Spending Time:  ", self.__spending)

avi = student("avi", 1/4, 72)
benjamin = student("benjamin", 3-12, 89)

avi = partTimeStudent()
avi.displayExamMark()
avi.displaySpendingTime()

benjamin = fullTimeStudent()
benjamin.displayExamMark()
benjamin.displayCreditHours()

