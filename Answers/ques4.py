#a program -if the lenght of a word is even then print "even"

st= "print every word in this sentence that has an even number of letters"

print("solution")

st_Lst=st.split()
for num in st_Lst:
    if len(num) % 2 == 0:
        print ("even")
    else:
        print(num)

end = "please press enter ; "

