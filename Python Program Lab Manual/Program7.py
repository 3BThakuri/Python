# check given number prime or not
n=int(input("Enter Number: "))



f=0

for i in range(2, n):

        if (n % i) == 0:

            f=1

           

            break



if f==1:

        print("not prime number")

else:

    print(" prime number")
