##############################################################################

## Chinese Zodiac Calculator

## Date Created: 1st October 2022

## Author: AVINASH RAMASH LAKHWANI

## Cohort: CAL2207D

## Student ID: 0028862

## Lecturer: Mr. ONG

## Function: This program will calculate the Chinese zodiac and output it accordingly

##############################################################################

animal_array = ['Monkey', 'Chicken', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare', 'Dragon', 'Snake', 'Horse', 'Goat']

def CheckZodiac(year):
    animal_index = year % 12
    return animal_index

def main():
    year = int(input("Enter a valid year: "))
    while year < 0  or year > 9999:
        print("That is not a valid year")
        year = int(input("Enter a valid year: "))
    zodiac = CheckZodiac(year)
    print("Zodiac sign: ", animal_array[zodiac])

check = ''
while check == '':
    main()
    check = str(input("Would you like to stop? Press any key to stop: "))
    
