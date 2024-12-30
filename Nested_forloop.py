#Nested for loop in python
'''Refers to a loop within a loop'''
list1 = [1,2,3]
list2 = [4,5,6]
for i in list1:
    for j in list2:
        print(i,j)
    print()

#Nested While loop in python
'''Is a while loop within a while loop'''
list1 = [1,2,3]
list2 = [4,5,6]
i = 0
while i < len(list1):
    j = 0
    while j < len(list2):
        print(list1[i],list2[j])
        j += 1
    print()
    i += 1


