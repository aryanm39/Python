#Write a program to check whether a given number is prime or not
'''
A Prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself
examples 2,3,5,7,11,13,... are all prime numbers'''

num = int(input("Enter an integer: "))
if num <= 1:
    print(f"{num} is not prime.")
elif num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is the factor of {num}.")
            print(f"{i} is the factor of {num}.")
            break

    else:
        print(f"{num} is prime.")
        

