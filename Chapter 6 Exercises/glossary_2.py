#Created 11/1/2022
#Exercise 6-4- Glossary 2: Clean up the code from Exercise 6-3 by replacing your series of print() calls with a loop that runs through the dictionary's keys and values. When you're sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.
programming_words = {'boolean':'a conditional test', 'dictionary':'a collection of key-value pairs', 'list':'a collection of items in a particular order', 'float':'any number with a decimal point', 'string':'a series of characters',
                     'integer':'any number without a decimal point',
                     'print()':'prints message inside the parentheses to console',
                     'conditional test': 'an expression that can be evaluated as True or False',
                     'equality operator':'returns True if the values on the left and right side of the operator match',
                     'immutable':'values that cannot change',
                     'tuple': 'an immutable list'                     
              }
for key,value in programming_words.items():
  print(f"{key}:\n\t{value}")
