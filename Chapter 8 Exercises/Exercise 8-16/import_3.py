from album import make_album as ma
#Created 11/29/2022 by Jared
#Exercise 8-16- Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
music_album = ma("J.I.D.","DiCapario2,", num_of_songs=14)
print(music_album)
