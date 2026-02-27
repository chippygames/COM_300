from calendar import month

from fontTools.misc.cython import returns
from matplotlib.testing.jpl_units import day


#week 2 task turned into a function
def task1():
    myage:int = 20
    # age = int(input("please enter your age"))
    age = 15
    if age < 18:
       return ("Remember, the current minimum age to buy alcohol is 18")
    elif age == myage:
            return ("Hey! We are the same age!")
    if age< 0:
         return ("wow, people start using computers early")

#fix ts bruh
def task2():
    day, month, year = birthday.split("/")
    day = int(input("please enter your day"))
    month = int(input("please enter your month"))
    year = int(input("please enter your year"))

    if day == 1 and month == 4:
    return ("it is april fools day")


    return



print (task2())
























#
# def calculate_discounted_price(price, discount_percent):
#     total = (price/20) * discount_percent
#
#     return price - total
#
# print(calculate_discounted_price(100, 0.2))
