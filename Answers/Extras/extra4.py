#this is a program to use list comprehension to create a list of words ending with "e"

print('Exercise 4: Words Ending with "e"')


x=["apple", "banana", "cherry", "date", "grape"]


y=[item for item in x if item[-1] == "e"]

print(y)

end = input("please press enter ; ")
