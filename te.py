Ticket = 4
age = int(input("please enter your age"))
Infantprice = Ticket - 4
childticket = Ticket / 2
pensionerticket = Ticket / 3
if age <= 5:
    print (F"infants pay {Infantprice} infants travel free")
if age >= 17:
    print (F"under 16s can buy a child ticket for {childticket}")
if age >= 65:
    print (F"passengers over 65 pay{pensionerticket}")
    if age <18 and age <= 65:
        print(F"passengers over 16 pay{Ticket}")
