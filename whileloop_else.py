'''When the while condition becomes false and the loop runs normally,then the else block will be executed'''
#Use of while loop with else
fruits = ['apple','banana','mango','strawberry']
fruits_len = len(fruits)
index =  0
while index < fruits_len:
    if fruits[index] == 'orange':
        print('Orange is available')
        break
    index += 1
else:
    print('Orange is not available.')
