#Finding HCF using Loops
'''
Highest Common Factor(HCF)
-> The highest Common Factor (HCF) of two numbers is the largest positive integer that perfectly divides the given 
two numbers
Example: 1. HCF of 12 and 18 is 6
            HCF of 12 and 15 is 3    '''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 < num2:
    smaller = num1
else:
    smaller = num2

for i in range(1, smaller + 1):
    if((num1 % i == 0) and (num2 % i == 0)):
        hcf = i
    
print(f"The HCF is {hcf}.")
