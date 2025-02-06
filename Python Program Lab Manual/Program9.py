# write a program to calculate sum of all numbers from 1 to given number

n=int(input("enter your number"))

sum=0
for x in range(1,n+1):
    sum=sum+x

print(sum)
