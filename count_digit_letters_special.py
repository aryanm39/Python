# Counting Digits,letters and Special Characters
'''Write a program that accepts a string and counts the number of digits,letters and special characters of that string'''
s = input("Enter a string: ")
d, l, o = 0, 0, 0
for c in s:
    if c.isdigit():
        d += 1
    elif c.isalpha():
        l += 1
    else:
        o += 1
    
print(f"Digits: {d}")
print(f"letters: {l}")
print(f"Other Characters: {o}")




