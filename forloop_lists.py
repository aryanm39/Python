#Iterating over a list
'''for loop can be used to iterate over a list.'''
cars = ['Audi','BMW','Toyota']
for car in cars:
    print(car)

#Iterating over a List using for loop and range()
'''for loop along with range() function can be used to iterate over a list'''
cars = ['Audi','BMW','Toyota']
for i in range(len(cars)):
    print(cars[i])

#List comprehension
'''List comprehension can produce the result in less lines of code.'''
cars = ['Audi','BMW','Toyota']
[print(car) for car in cars]
