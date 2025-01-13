"""Write a program to input age of person and display message as 
follows 
‐ If age < 12 print You are Kid 
‐ If age between 12 to 17 print You are teenager 
‐ If age between 18 to 60 print you are Adult 
 -If age > 60 print You are Senior Citizen"""

age=int(input("Enter your age: "))

if(age<12):
    print("You are Kid")
elif (12<=age<= 17):
    print("You are teenager")
elif 18<=age<=60:
    print("You are Adult")
else:
    print("You are Senior Citizen")
