#Created 12/2/2022 by Jared
#Exercise 9-13- Make a class Die with one attribute called sides, which hasa a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
#   Make a 10-sided die and a 20-sided die. Roll each die 10 times.
import die
six_die = die.Die()
print("Rolling six-sided die 10 times...")
for num in range(1,11):
    six_die.roll_die()
    
ten_die = die.Die(sides=10)
print("Rolling ten-sided die 10 times...")
for num in range(1,11):
    ten_die.roll_die()
    
twenty_die = die.Die(20)
print("Rolling twenty-sided die 10 times...")
for num in range(1,11):
    twenty_die.roll_die()
