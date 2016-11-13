#this is a game where you can chose a number and see if you hit the jackpot!!
import random
dienumber = random.randint(1,6)
number = int ( input ("please input a number from one to six that you think will come up"))
if number == dienumber:
    print("congratulations you won 2000 pounds")
elif number <= dienumber:
    print("congratulations you won 20 pounds")
elif number >= dienumber:
    print("sorry you didnt win anything")
