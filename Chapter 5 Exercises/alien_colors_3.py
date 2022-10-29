#Created 10/28/2022
#Exercise 5-5- Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#  If the alien is green, print a message that the player earned 5 points.
#  If the alien's color is yellow, print a statement that the player just earned 10 points.
#  If the alien's color is red, print a message that the player earned 15 points.
#Write three versions of the program, making sure each message is printed for the appropriate color alien.
alien_color = 'red'
if alien_color == "green":
  print("Shooting the alien gave you 5 points!")
elif alien_color == "yellow":
  print("Shooting the alien gave you 10 points!")
else:
  print("Shooting the alien have your 15 points!")
