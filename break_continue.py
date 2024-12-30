#Break and continue Statements in Python
'''Used to terminate the running loop'''
numbers = list(range(0,100))
for number in numbers:
    if number > 50:
        break
    print(number,end=' ')

while True:
    num = input("Enter the number (q for quit): ")
    if num =='q':
        break
    print(num)

#Continue Statement
'''Used to skip the current iteration of the loop'''
for i in range(5):
    if i == 2 or i == 4:
        continue
    print(i)

n = 0
while n <= 10:
    n += 1
    if n % 2 != 0:
        continue
    print(n,end=' ')
    