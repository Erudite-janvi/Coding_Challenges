from math import factorial
n =  int(input("enter the number of rows "))
for i in range (n):
    for space in range(n-i):
        print(" ",end="")
    for j in range(i+1) :
        ncr = factorial(i) // (factorial(j)*factorial(i- j))
        print(ncr, end=" ")  
    print()
