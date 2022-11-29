#Created 11/29/2022 by Jared
#Exercise 8-12- Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich thats being order. Call the function three times, using a different number of arguments each time.
def make_sandwich(*contents):
  print("This sandwich has the following on it:")
  for content in contents:
    print(f"\t{content}")
make_sandwich("meatballs","marinara sauce","cheese")
make_sandwich("turkey","mustard","lettuce","onions","cheese")
make_sandwich("ham","mustard","lettuce","bacon","cheese")
