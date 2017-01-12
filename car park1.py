#this is a car park machine
import time
print("hello, welcome to the best car park in the world, this is a very exclusive car park")
print("as the security in the car park is the best in the world you will have to pay 10000 pounds an hour.")


moneyentered = float(input("please enter the amount of money that will pay for your stay"))
print("you have entered",moneyentered)


while moneyentered < 10000:
        morecoins = float(input("please enter more money"))
        print("you have entered:")
        print(morecoins)
        moneyentered = moneyentered + morecoins
        if moneyentered < 10000:
                evenmorecoins = float(input("Can we please have even more money, you didnt enter enough"))
                moneyentered = moneyentered + evenmorecoins
        else:
                moneyentered >= 10000
                



change = moneyentered - 10000
print("your change is:")
print(change)

print("please wait for the ticket to print")
time.sleep(2)


print("thanks for buying a ticket in the most secure car park in the world")
print("here is your ticket:")
print("|-----------------------------------------------------------------------|")
print("|        place: A3                                time allowed:1 hr     |")
print("|                                                                       |")
print("|                                                                       |")
print("|                thank you for using our car park                       |")
print("|_______________________________________________________________________|")


