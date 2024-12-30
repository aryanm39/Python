#for loop vs while loop
'''for loop ->needs an iterable object to iterate
Syntax of for loop
for var in iterable:
    #do something
while loop->executes based on some condition
Syntax of while loop
while condition:
    #do something'''

'''for loop is used when the number of iterations is known in advance
while loop is used when the number of iterations is not known in advance'''

for i in range(1,6):
    print(i)

while True:
    n = input("Enter the number: ")
    if n == 'q':
        break
    print(n)

'''Both for and while loop can run infinite times'''
items = [0]
for item in items:
    print(item)
    items.append(item)

item = 0
while True:
    print(item)
