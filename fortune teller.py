#This programme chooses a random number between 1 aand 6 and then tells a story
#that will happen according to entered stories below.
import time
import random
print("Hello Fellow Dear Human Being.")
time.sleep(3)
print("This is a programme by Me, and it is going to tell you a fortune")
print("Trust me i am a magician")
print("your number iiiiiiissssssssssssssss")
time.sleep(10)
print(answer)
print("your fortune is")
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
