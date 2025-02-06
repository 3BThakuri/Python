# Program to find the factorial of a given number

n=int(input("enter number: "))
if(n==0):
    print("you have entered zero")
elif(n<0):
    print("you have entered negetive value")
else:
    fact=1

    for x in range(1,n+1):
        fact = fact * x

    print("the factorial is:",fact)
