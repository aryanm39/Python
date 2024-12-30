#Printing Right Triangle Number Pattern
'''Write a program to print a right triangle number pattern as shown:'''

rows = int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print('')