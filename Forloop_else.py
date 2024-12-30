#For loop with else in Python
'''The else block will be executed only when the loop is NOT terminated abruptly by the break keyword'''

#Use of for loop with else
fav_languages = ['Python','C','Java','Ruby']
for language in fav_languages:
    if 'Java' == language:
        print("I like Java.")
        break
else:
    print("I don't like Java.")
    