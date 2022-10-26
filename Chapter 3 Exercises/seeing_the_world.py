#Created 10/25/2022 by Jared
# Exercise 3-8- Seeing the World: Think of at least five places in the world you'd like to visit.
#  Storer the locations in a list. Make sure the list is not in alphabetical order.
#  Print your list in its original order. Don't worry about printing the list neatly; just print it as a raw Python list.
#  Use sorted() to print your list in alphabetical order without modifying the actual list.
#  Show that your list is still in its original order by printing it.
#  Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#  Show that your list is still in its original order by printing it again.
#  Use reverse() to change to order of your list. Print the list to show that its order has changed.
#  Use reverse() to change the order of your list again. Print the list to show it's back to its original order.
#  Use sort() to change your list so it's sorted in alphabetical order. Print the list to show that its order has been changed.
#  Use sort() to change your list so it's stored in reverse-alphabetical order. Print the list to show that its order has changed.
want_to_go = ["tokyo", "london", "greece", "aspen", "italy"]
print(f"Original order: {want_to_go}") #Printing in original order
print(f"Alphabetical order: {sorted(want_to_go)}") #Printing in alphabetical order
print(f"Current order: {want_to_go}") #Printing proof that the list is untouched
print(f"Reverse-alphabetical order: {sorted(want_to_go, reverse=True)}") #Printing in reverse alphabetical order
print(f"Current order: {want_to_go}") #Printing proof that the list is untouched
want_to_go.reverse() #Reverse the list
print(f"Reverse order: {want_to_go}") #Printing the list in reverse order
want_to_go.reverse() #Reverse the list again
print(f"Reversed twice order: {want_to_go}") #Printing the reversed list in reverse
want_to_go.sort() #sort the list
print(f"Sorted list: {want_to_go}") #Printing the list after its been sorted
want_to_go.sort(reverse=True) #sort the list in reverse order
print(f"Reversed sorted list: {want_to_go}") #Printing reversed sorted list
