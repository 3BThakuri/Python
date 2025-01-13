#Takes three values from the user and finds the Minimum and Maximum numbers
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

min=min(num1, num2, num3) 
max=max(num1, num2,num3)

print("The minimum number is:",min)
print("The maximum number is:",max)
