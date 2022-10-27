#Created 10/26/2022
#Exercise 4-5 - Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

one_to_million = list(range(1, 1000001))
print(f"min element in list: {min(one_to_million)}")
print(f"max element in list: {max(one_to_million)}")
print(f"sum of the list: {sum(one_to_million)}")
