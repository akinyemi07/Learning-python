#a program to print the list of vowels with list comprehension.

st = 'list comprehensions are awesome' 

vowels = "aeiouAEIOU"

x=[char for char in st if char.isalpha() and char in vowels]

print(x)

print("-".join(x))
