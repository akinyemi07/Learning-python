#fizzbuzz

print("fizzbuzz")

print("a program to print fizz and buzz for multiples of three and five")

for num in range(1,1001):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num}= fizzbuzz!")
    elif num % 5 == 0:
        print (f"{num}= Buzz!")    
    elif num % 3 == 0:
        print (f"{num}= Fizz!")
    else:
        print("--")

end= input("please press enter ")

        
