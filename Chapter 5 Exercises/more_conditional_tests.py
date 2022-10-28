#Created 10/27/2022
#Exercise 5-2- More Conditional Tests: Write more tests. Have at least one true and one false result for each of the following:
#  Tests for equality and inequality with strings
#  Tests using the lower() method
#  Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
#  Tests using the and keyword and the or keyword
#  Test whether an item is in a list
#  Test whether an item is not in a list
a = 1
b = 10
c = 1
list = ["alpha", "beta", "gamma"]
print("Testing if list[0] isnt alpha:")
print(list[0] != "alpha")
print("Testing if list[2] is gamma:")
print(list[2] == "gamma")
print("Testing if list[1] is beta in lowercase:")
print(list[1].lower() == "beta")
print("Testing if list[0] is delta in lowercase:")
print(list[0].lower() == "delta")
print("Testing if a == b:")
print(a == b)
print("Testing if a != b")
print(a != b)
print("Testing if a < b:")
print(a < b)
print("Testing if c > b")
print(c > b)
print("Testing if a < b and a == b:")
print((a < b) and (a == b))
print("Testing if a == c or c == b")
print((a == c) or (c == b))
print("Testing if omicron is in list:")
print("omicron" in list)
print("Testing if alpha is in list:")
print("alpha" in list)
