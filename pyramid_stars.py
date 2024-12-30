#Print the full Pyramid of stars
'''Write a program to print the full pyramid of stars as shown:
number of whitespaces before the first star = number of rows - row number '''

rows = int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for space in range(1,rows-i+1):
        print(end=' ')

    for star in range(1,i+1):
        print("*",end=' ')
    print('')


