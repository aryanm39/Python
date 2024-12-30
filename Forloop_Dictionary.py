#for loop can be used to iterate over a dictionary

course = {'name':'Python','instructor':'Jaspreet'}
for x in course:
    print(x)

#Accessing values of a Dictionary
'''values can be accessed using square-bracket notation'''
course = {'name':'Python','instructor':'Jaspreet'}
for x in course:
    print(course[x])

#Values can also be accessed using values() method
course = {'name':'Python','instructor':'Jaspreet'}
for y in course.values():
    print(y)

#Accessing keys of a Dictionary
'''Keys can be accessed using keys() method'''
course = {'name':'Python','instructor':'Jaspreet'}
for x in course.keys():
    print(x)

#Accessing keys and values of a Dictionary
'''Keys and values can be accessed using items() method'''
course = {'name':'Python','instructor':'Jaspreet'}
for x,y in course.items():
    print(x, y)

