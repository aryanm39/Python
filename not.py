#Logical NOT with Boolean value

x = False
if not x:
    print("x is false.")


#Logical NOT with a string
name = 'John'
if not name:
    print("No name.")
else:
    print(f"Your name is {name}.")


#Logical NOT with a List,Dictionary or Tuple
names = ['John','Mike','Sarah']
if not names:
    print("No names.")
else:
    print(f"There are a total of {len(names)} names.")
