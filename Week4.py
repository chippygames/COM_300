
#task 1
# count = 1
#
#
# while count <= 20:
#     print(count)
#     count += 1
#

#task 1.2
# count = 1

# count = 5
# while count <= 15:
#     print(count)
#     count += 1



# task 1.3
#

#
# count = 1
# while count <= 21:
#     print(count)
#     count += 2

 # task 1.4
#
# count = 10
# while count >= -1:
#     print(count)
#     count -= 1






#finish this bs
# task 2

# timestable = int(input("Enter timestable number: "))
# for i in range(0,13):
#    awnser = i * timestable
#    print(f"{i} x {timestable}{awnser}" )

def first_func():
    state = 1
    while state == 1:

        age = int(input("please enter your age"))
        Ticket = 4
        Infantprice = Ticket - 4
        childticket = Ticket / 2
        pensionerticket = Ticket / 3
        if age <= 5:
            print(F"infants pay {Infantprice} infants travel free")
        elif age < 16:
            print(F"under 16s can buy a child ticket for {childticket}")
        elif age >= 65:
            print(F"passengers over 65 pay{pensionerticket}")
        else:
            print(F"passengers over 16 pay{Ticket}")

        state = int(input("please enter 1 if you would like the loop to continue and 0 if you want it to stop "))


first_func()

