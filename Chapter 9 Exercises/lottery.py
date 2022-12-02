#Created 12/2/2022 by Jared
#Exercise 9-14- Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
from random import choice
characters = ['j','e','k','d','b', 89, 95, 21, 22, 81, 47, 15, 100, 98, 39]
print("If you picked any of the following letters or numbers, you won a prize:")
for winners in range(1,5):
    print(choice(characters))
