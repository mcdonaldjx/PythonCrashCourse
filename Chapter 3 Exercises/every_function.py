#Created 10/25/2022 by Jared
# Exercise 3-9- Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
languages = ["english", "spanish","french","japanese","valerian","dothraki"]
print(f"Original order: {languages}")
print(f"Alphabetical order: {sorted(languages)}")
print(f"Original order: {languages}")
print(f"Reverse-alphabetical order: {sorted(languages, reverse=True)}")
print(f"Original order: {languages}")
languages.sort()
print(f"Sorted order: {languages}")
languages.sort(reverse=True)
print(f"Reverse-sorted order: {languages}")
