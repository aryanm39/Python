#Write a program to check whether the given string is a palindrome or not
'''
A Palindrome is a word,a sentence,or a number that reads the same backwords as forwords
Ex. level,madam,1221,etc.'''
s = input("Enter a string: ")
s = s.replace(" ","").lower()
start = 0
end = len(s) - 1
flag = True
while start < end:
    if s[start] != s[end]:
        flag = False
    start += 1
    end -= 1

if flag:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    

