
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
#
#     num = int(input("please enter a number between 1,20"))
#     num2 = int(input("please enter a second number between 1,20"))
#     num_total = num + num2
#     if num > 20:
#         if num2 > 20:
#             print("sorry the numbers needs to be less than 20")
#     for i in range(1,21):
#         for j in range(1,21):
#             if num_total == j:
#                 print("x", end="")
#             else:
#                 print("-", end="")
#                 if num == i:
#                     print("x",end="")
#                 else:
#                     print("-", end="")
#
#
#atempted how did that happen 60-69





#add comments




# def assessment_3():
#     while True:
#         print("please enter the letter which corresponds with your choice\nA-calculate the area of a rectange\nB-calculate the area of a circle\n C-Display a multiplication Table\n D- find the mean of three numbers\n X- Exit the program")
#         userinput =  input("")
#         if userinput == "a".lower():
#             Width =  int(input("please enter the width of the rectangle"))
#             Height = int(input("please enter the height of the rectangle"))
#             Area_Rectangle = Width * Height
#             print (f"the area of the rectangle is {Area_Rectangle}")
#         elif userinput == "b".lower():
#            radius = int(input("please enter the radius of the circle"))
#            pi = 3.14159
#            Area_Circle = pi * (radius ** 2)
#            print (f"the area of the circle is {Area_Circle}")
#         elif userinput.lower() == "c".lower():
#             Number = int(input("Please enter a number between 1,10"))
#             for i in range(1,11):
#                 Times_table = Number * i
#                 print (f"the multiplication table for this number is {Times_table}")
#         elif userinput == "d".lower():
#             Num_1 = int(input("please enter a number"))
#             Num_2 = int(input("please enter a number"))
#             Num_3 = int(input("please enter a number"))
#             result = (Num_1 + Num_2 + Num_3) / 3
#             print (f"the mean of the numbers  is {result}")
#         if userinput == "x".lower():
#             break
#         elif userinput not in str(["A","B","C","D","X"]):
#             print ("Sorry, your input was not recognised, please enter either A,B,C,D,X")
#

# finished
#sike upper lower case or whatever needs to be fixed.



# def assessment_4():
#     coordinateX = int(input("please enter a coordinate between 1 and 10"))
#     coordinateY = int(input("please enter a coordinate between 1 and 10"))
#     while True:
#      for row in range (1,11):
#          for col in range(1,11):
#             if coordinateY == row and coordinateX == col:
#                 print("X", end="")
#             else:
#                 print("-", end="")
#          print()
#
#
#     user_move = (input("'w','a','s', 'd' or 'x'")).lower()
#
#     if user_move == "w":
#         if coordinateY > 1:
#             coordinateY -= 1
#
#         elif user_move == "a":
#             if coordinateX > 1:
#                 coordinateX -= 1
#
#     elif user_move == "s":
#         if coordinateY < 1:
#             coordinateY += 1
#
#     elif user_move == "d":
#         if coordinateX < 1:
#             coordinateX += 1
#
#     elif user_move == "x":
#     break

#what??? why not work

# def assessment_5():
#     # pain fix later "loop everything so it updates after all questions done
#fuck that
#60-69 list limit


    # math_List = []
    # while True:
    #     user_Input = input("please enter a choice from the menu\nA-add numbers\nB-Display all values\nC-Replace one number\nD-Calculate the mean\nE-Find the largest number in the list\nF-All instances of the number you selected will be deleted.\nX-Exit")
    #
    #
    #     if user_Input.lower() == "a":
    #         how_many =(int(input("how many numbers you would like to add\n")))
    #         for i in range(how_many):
    #             number = int(input("please enter your number"))
    #             math_List.append(number)
    #         print (math_List)
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
    #       replace_delete = int(input("please what number would you like to replace"))
    #       if replace_delete == (math_List):
    #           math_List.remove(math_List[replace_delete])
    #         max_number = 20
    #     elif math_List > max_number:
    #         print ("only a maximum of 20 numbers are allowed witihin the list")
    #
    #     else: user_Input.upper() == "A", "B", "C", "D", "E", "X","F",
    #     print("Please enter a valid letter from the menu.")



def assessment_6():

    arr = [6, 5, 3, 1, 2]
    for r in range(len(arr)):
        if arr[r] < arr[0]:
            temp_value = arr[0]
            temp_Value1 = arr[1]
            temp_value2 = arr[2]
            temp_value3 = arr[3]
            temp_value4 = arr[4]
            arr[0] = arr[r]
            arr[r] = temp_value
        for d in range(len(arr)):
            if arr[d] < arr[1]:
                arr[1] = arr[d]
                arr[d] = arr[temp_Value1]
        for c in range(len(arr)):
            if arr[c] < arr[2]:
                arr[2] = arr[c]
                arr[c] = arr[temp_value2]
        for e in range(len(arr)):
            if arr[e] < arr[3]:
                arr[3] = arr[e]
                arr[e] = arr[temp_value3]
        for f in range(len(arr)):
            if arr[f] < arr[4]:
                arr[4] = arr[f]
                arr[f] = arr[temp_value4]

    print (arr)


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
    # print(assessment_2())
    # print(assessment_3())
    # print(assessment_4())
    # print(assessment_5())
    print(assessment_6())
    # print(assessment_7())