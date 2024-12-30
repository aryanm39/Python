#range() function-> returns a series of numbers
'''syntax: range(start,stop,step) -default:start=0,stop=not included,step=1:increment is 1'''

#For loop with range(stop)
'''Generates a sequence of integers starting from 0 to stop - 1
for i in range(5):
    print(i)
print("Done!")
'''
#For loop with range(start,stop)
'''Generates a sequence of integers starting from start to stop - 1
for i in range(1,6):
    print(i)
print("Done!")
'''

#For loop with range(start,stop,step)
'''Generates a sequence of integers starting from start,incremented by step,and stopped at stop - 1'''
for i in range(1,10,2):
    print(i)
print("Done!")

#Points to remember
'''
-> The range() function only works with integer arguments.
-> All three arguments can be positive or negative.
-> The step value cannot be zero
'''