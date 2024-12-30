#Write a program to print the Pascal's triangle as shown:

# nCr = n!/r!(n-r)!

from math import factorial
rows = int(input("Enter the number of rows: "))
for n in range(rows):
    for space in range(1,rows-n):
        print(end=' ')
    
    for r in range(n+1):
        ncr = factorial(n) // (factorial(r) * factorial(n - r))
        print(ncr,end=' ')
    
    print('')














