#Created 11/1/2022
#Exercise 6-3- Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
# Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line.
programming_words = {'boolean':'a conditional test', 'dictionary':'a collection of key-value pairs', 'list':'a collection of items in a particular order', 'float':'any number with a decimal point', 'string':'a series of characters' 
              }
for p_word in programming_words:
  print(f"{p_word}:\n\t{programming_words[p_word]}")
