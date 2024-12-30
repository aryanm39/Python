#Problem Statement
'''Write a program to separate even and odd numbers stored in a list into two diffrent lists'''
li = list(range(1,25))
even_numbers = []
odd_numbers = []
for item in li:
    if item % 2 == 0:
        even_numbers.append(item)
    else:
        odd_numbers.append(item)
print(odd_numbers)
print(even_numbers)

