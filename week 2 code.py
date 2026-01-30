import datetime

myage:int = 20
age = int(input("please enter your age"))
if age < 18:
    print("Remember, the current minimum age to buy alcohol is 18")
elif age == myage:
        print ("Hey! We are the same age!")
if age< 0:
    print ("wow, people start using computers early")

day = int(input("please enter your day"))
month = int(input("please enter your month"))
year = int(input("please enter your year"))
if day == 1 and month == 4:
    print ("it is april fools day")

E = "start"
match E:
    case day = 1 and month == 4:
        print("it is april fools day")
    case day = 1 and month == 1:
        print ("its new years!")
    case day = 15 and month == 10:
        print ("its my birthday")
    case day = 4 and month == 5
        print ("may the 4th be with you")
    case _ :
        print("please enter a day and month")



# speed = 32
# speedlimit = 21
# if speed <= speedlimit:
#     print("please continue to drive safely")
# elif speed-speedlimit  >= 10:
#     print(f"you were moving at speed{speed}the speedlimit is {speedlimit}you will now get a ticket and a possible court summon")
# else:
#     print (f"your speed is {speed},the speed limit is {speedlimit}. your're speeding! Ticket for you!")
#
#
#
#

