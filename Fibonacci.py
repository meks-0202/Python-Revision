def fib(n):
    a=0
    b=1
    if n ==0 or n<0:
        print("Error")
    elif n == 1:
        print(a)
    else:
        print(a, end=" ")
        print(b, end=" ")
        for i in range(2, n):
            print(a+b, end=" ")
            c = a+b
            a = b
            b = c
            i+=1
n=int(input())
fib(n)

#function to find the nth fibonacci number
def nth(n):
    if n<0:
        print("Error")
    elif n== 1:
        return 0 
    elif n == 2: 
        return 1
    else: 
        return nth(n-1) + nth(n-2)

print("\n",nth(n))
