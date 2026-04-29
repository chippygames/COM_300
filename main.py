
from character import Character
#
# def assessment_1():
#     order_Value = int(input("please enter your order number"))
#     distance = int(input("please enter your distance"))
#     cost = 3.95
#
#     # total_cost = cost + deliveryfee
#     if distance <= 10 and  order_Value >= 100:
#         print ("delivery is free")
#         # return 0
#     elif distance <= 10 and order_Value < 100:
#         print (" delivery is £5")
#         # return 5
#     elif distance < 20:
#         print("delivery is 10")
#         # return 10
#     elif distance <= 30:
#         print("delivery is 15")
#         # return 15
#     else:
#         diffrence = distance - 30
#         extra = distance * 0.5
#         ammount = 15 + extra
#         print (f"your delivery cost{ammount}")
#     #
#     # free_delivery = 10
#     # if  distance  and order_Value <= 100:
#     # print(f"the total cost is {total_cost}")
#     # print(f"delivery cost is {deliveryfee}")
#     # print(f"you are {distance} miles away")
#     # print(f"you paid {cost} dollars")
#     # return
#

# def assessment_2():

#     num = int(input("please enter a number between 1,20"))
#     num2 = int(input("please enter a second number between 1,20"))
#     num_total = num + num2
#     if num > 20:
#         if num2 > 20:
#             print("sorry the numbers needs to be less than 20")
#     for i in range(1,21):
#         print("-", end="")
#         if num == i:
#             print("x",end="")
#         elif num_total == i:
#             print("x",end="")
#         else:
#             print("-", end="")


#easy





#add comments




# def assessment_3():
#     while True:
#         print("please enter the letter which corresponds with your choice\nA- Calculate the area of a rectangle\nB- Calculate the area of a circle\nC- Display a multiplication Table\n D- Find the mean of three numbers\n X- Exit the program")
#         userinput =  input("")
#         if userinput.lower() == "a":
#             Width =  int(input("please enter the width of the rectangle"))
#             Height = int(input("please enter the height of the rectangle"))
#             Area_Rectangle = Width * Height
#             print (f"the area of the rectangle is {Area_Rectangle}")
#         elif userinput.lower() == "b":
#            radius = int(input("please enter the radius of the circle"))
#            pi = 3.14159
#            Area_Circle = pi * (radius ** 2)
#            print (f"the area of the circle is {Area_Circle}")
#         elif userinput.lower() == "c":
#             Number = int(input("Please enter a number between 1,10"))
#             for i in range(1,11):
#                 Times_table = Number * i
#                 print (f"the multiplication table for this number is {Times_table}")
#         elif userinput.lower() == "d":
#             Num_1 = int(input("please enter a number"))
#             Num_2 = int(input("please enter a number"))
#             Num_3 = int(input("please enter a number"))
#             result = (Num_1 + Num_2 + Num_3) / 3
#             print (f"the mean of the numbers  is {result}")
#         if userinput.lower() == "x":
#             break
#         elif userinput.lower() not in str(["a","b","c","d","x"]):
#             print ("Sorry, your input was not recognised, please enter either A,B,C,D,X")


# finished
#sike upper lower case or whatever needs to be fixed.



# def assessment_4():
#
#     coordinateX = int(input("please enter a coordinate between 1 and 10"))
#     coordinateY = int(input("please enter a coordinate between 1 and 10"))
#     while True:
#         for row in range (1,11):
#              for col in range(1,11):
#                 if coordinateY == row and coordinateX == col:
#                     print("X", end="")
#                 else:
#                     print("-", end="")
#              print()
#         print("please enter where you would like the x to go next")
#         user_move = (input("'w','a','s', 'd' or 'x'"))
#
#         if user_move.lower() == "w":
#             if coordinateY > 1:
#                     coordinateY -= 1
#
#         elif user_move.lower() == "a":
#             if coordinateX > 1:
#                 coordinateX -= 1
#
#         elif user_move.lower() == "s":
#             if coordinateY > 1:
#                 coordinateY += 1
#
#         elif user_move.lower() == "d":
#             if coordinateX > 1:
#                 coordinateX += 1
#
#         elif user_move.lower() == "x":
#             break


def assessment_5():
    # pain fix later "loop everything so it updates after all questions done
    #
    #
    # math_List = []
    # while True:
    #     user_Input = input("please enter a choice from the menu\nA-add numbers\nB-Display all values\nC-Replace one number\nD-Calculate the mean\nE-Find the largest number in the list\nF-All instances of the number you selected will be deleted.\nX-Exit")
    #     if len(math_List) > 19:
    #         print("only a maximum of 20 numbers are allowed within the list")
    #
    #     if user_Input.lower() == "a":
    #         how_many =(int(input("how many numbers you would like to add\n")))
    #         for i in range(how_many):
    #             number = int(input("please enter your number"))
    #             math_List.append(number)
    #         print (math_List)
    #
    #
    #
    #     elif user_Input.lower() == "b":
    #         for i in math_List:
    #             print(i)
    #
    #     elif user_Input.lower() == "c":
    #         order_new = (int(input("please enter what element you would like to replace")))
    #         new_number = (int(input("please enter your number")))
    #         print (math_List[order_new])
    #         math_List[order_new] = new_number
    #         print (math_List)
    #
    #     elif user_Input.lower() == "d":
    #         count = 0
    #         tally = 0
    #         for i in range(len(math_List)):
    #             tally += math_List[i]
    #             count += 1
    #         awnser = tally/count
    #         print(awnser)
    #
    #     elif user_Input.lower() == "e":
    #         big_number = max(math_List)
    #         print(f"the largest number in the list is {big_number}")
    #
    #     elif user_Input.lower() == "x":
    #             print("thank you for using this program")
    #             break
    #     elif user_Input.lower() == "f":
    #         if not math_List:
    #             print("List is empty.")
    #         else:
    #             delete_num = int(input("Enter the number you want to delete: "))
    #             math_List = [x for x in math_List if x != delete_num]
    #             print("Updated list:", math_List)
    #
    #     else: user_Input.upper() == "A", "B", "C", "D", "E", "X","F",
    #     print("Please enter a valid letter from the menu.")



def assessment_6():

    arr = [6, 5, 3, 1, 2]
    for r in range(len(arr)):
        if arr[r] < arr[0]:
            temp_value = arr[0]
            temp_Value1 = arr[1]
            arr[0] = arr[r]
            arr[r] = temp_value
        for d in range(len(arr)):
            if arr[d] > arr[d+1]:
                arr[1] = arr[d]
                arr[d] = temp_Value1


# def assessment_7():
#
#     player1 = Character("luke",100,50,100)
#     player2 = Character("bob",100,50,100)
#
#
#     print(player1.info())
#     print(player2.info())
#
#     player1.heal(200)
#
#     player1.attack_target(player2)
#
#     print(player1.info())








if __name__ == "__main__":

    # print(assessment_1())
    #  print(assessment_2())
    # print(assessment_3())
    # print(assessment_4())
    # print(assessment_5())
    #print(assessment_6())
    # print(assessment_7())