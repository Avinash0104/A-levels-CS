animal_array = ['Monkey','Chicken','Dog','Pig','Rat','Ox','Tiger','Hare','Dragon','Snake','Horse','Goat']
def main():
    inputValidity = False
    while inputValidity == False:
        year = int(input('Please enter a year between 0 and 9999: '))
        if year >= 0 or year <= 9999:
            inputValidity = True
        else:
            print('Invalid input, please enter a year between 0 and 9999')
            inputValidity = False
        CheckZodiac(year)
        cont = input('Press enter if you want to continue')
        while cont == '':
            main()  
        print('Thanks for using the zodiac calculator')

def CheckZodiac(year):
    animal_index = year%12
    animal = animal_array[animal_index]
    print('The animal for this year is',animal)
main()
