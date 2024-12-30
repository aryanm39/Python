#Accessing Characters of a string
'''for loop can be used to access all characters of a string'''
name = "John"
for c in name:
    print(c,end=' ')

#Iterating a String in Reverse Order
'''Slicing can be used to reverse a string'''
name = "John"
for c in name[::-1]:
    print(c, end=' ')

#Accessing words of a String
'''split() function can be used to split a string into words. '''
sentence = "Lorem ipsum dolor sit amet, consectetur."
count = 0
for word in sentence.split():
    count += 1
print(f"There are {count} words in the sentence.")
