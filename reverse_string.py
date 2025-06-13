string = input("Enter a string: ")
rev_string = ""
len = len(string) - 1
while len >= 0:    # while loop
    rev_string += string[len]
    len -=1
print(rev_string)

for i in range(len):    #for loop
    rev_string += string[len]
    len -=1
print(rev_string)

print(string[::-1])    #using python func
