# compound interest

p=int(input("Enter principal:"))
r=int(input("Enter rate:"))
n=int(input("enter time:"))

Amount=p*((1+(r/100))**n)

ci=Amount-p

print("Compound Interest is:",ci)


