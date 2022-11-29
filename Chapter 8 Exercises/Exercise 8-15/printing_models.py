import printing_functions
#Created 11/29/2022 by Jared
#Exercise 8-15- Printing Models: Put the functions for the example printing_models.py in a seperate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
#Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)

#Display all completed models.
printing_functions.show_completed_models(completed_models)
