#a program to use list comprehension to print the following -given a list of words ["hello", "world", "python", "is", "fun"], create a list that contains the length of each word.

word_lst = ["hello", "world", "python", "is", "fun"]

new_lst =[len(item) for item in word_lst]

print(new_lst)
