#Created 10/26/2022
#Exercise 4-9 - Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubes = [x**3 for x in range(1,11)]
for cube in cubes:
  print(cube)
