#program to find the HCF of two numbers using Euclidean algorithm
'''
step1 : Divide the greater number by smaller number and take the remainder
step2 : Divide the smaller number by the remainder
step3 : Repeat until remainder is 0
 Example : 15/12 -> remainder=3, 
           12/3 -> remainder=0
           HCF = 3 
'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 < num2:
    num1, num2 = num2, num1   #tuple unpacking
while (num2 != 0):
    num1, num2 = num2, num1 % num2

print(f"The HCF is {num1}.")


