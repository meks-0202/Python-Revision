number = int(input("Enter a number: "))
len = len(str(number))
#print (number, len)
sum =0 
temp = number # eg 153
while temp > 0:
    digit = temp % 10     # this gives 3, 5, 1 individialy in each loop
    sum += digit ** len    # digit ^lenght of number eg. 3^3, 5^3, 1^3
    temp = temp // 10    # gives the remaining number 15, 1

if sum == number:
    print(True)
else:
    print(False)
