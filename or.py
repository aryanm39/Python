# Logical OR with conditionals

today = 'Sunday'
if today == 'Saturday' or today == 'Sunday':
    print("It's a weekend!")

#
today = 'Monday'
if today == 'Saturday' or today == 'Sunday':
    print("It's a Weekend!")
else:
    print("It's a weekday!")

#
today = 'Tuesday'
if today == 'Saturday' or today == 'Sunday':
    print("It's a holiday!")
elif today == 'Monday' or today == 'Friday':
    print("work 2 hours extra.")
else:
    print("Normal Work hours.")