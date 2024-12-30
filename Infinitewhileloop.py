#The Infinite while loop in python
'''
A while loop can run infinitely if the condition never becomes false
n  = 100
while True:
    print(n)
    n -= 1
'''
#breaking infinite while loop
while True:
    line = input("Enter the line (type 'q' to quit): ")
    if line == 'q':
        break
    print(line)