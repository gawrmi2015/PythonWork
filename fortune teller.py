#This programme chooses a random number between 1 aand 6 and then tells a story
#that will happen according to entered stories below.
import random
answer = random.randint(1,6)
if answer == 1:
    print("you will make a new friend this week")
elif answer == 2:
    print("you will do well in your GCSEs")
elif answer == 3:
    print("you will find something you thougt you lost")
elif answer == 4:
    print("you will get over 3 credits this week")
elif  answer == 5:
    print("you will pass your next test that you take")
else answer == 6:
    print("you will find over 200 pounds on the floor")
