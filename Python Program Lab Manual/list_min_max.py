# Write a Program to create a list from user input and print the min and max numbers

list=[]

m=int(input("Enter how many elements you want to add: "))

for i in range(m):
    n=int(input(f"Enter a number {i + 1}: "))
    list.append(n)

print("\nList:",list)
print("\nMaximum number is:",max(list))
print("Minimum number is:",min(list))
