#
# def calculate_fee(distance):
#     if distance <= 10:
#         return 0
#     elif distance <= 10:
#         return 10
#     elif distance <= 20:
#         return 15
#     elif distance <= 30:
#         return 15
#     elif distance < 40:
#         return 0
#
#     return
#
#
# def assessment_1():
#     order_Value = int(input("please enter your order number"))
#     distance = int(input("please enter your distance"))
#     cost = 3.95
#
#     deliveryfee = calculate_fee(distance)
#
#
#     total_cost = cost + deliveryfee
#
#     print(f"the total cost is  {total_cost}")
#     print(f"delivery cost is {deliveryfee}")
#     print(f"you are {distance} miles away")
#     print(f"you paid {cost} dollars")
#     return
#finished?
#simple drone delivery service


# def assessment_2():
#     num = int(input("please enter a number between 1,20"))
#     if num > 20:
#         print("sorry the number needs to be less than 20")
#     else:
#         for i in range(1,21):
#             if num == i:
#                 print("x",end="")
#             else:
#                 print("-",end ="")
#         if num > 20:
#
#             print("sorry the number needs to be less than 20")
# #50-59 screenshot remeber
# #add comments




# def assessment_3():
#     print("please enter the letter which corresponds with your choice\nA-calculate the area of a rectange\nB-calculate the area of a circle\n C-Display a multiplication Table\n D- find the mean of three numbers")
#     userinput =  input("")
#     if userinput == ("A").lower():
#         Width =  int(input("please enter the width of the rectangle"))
#         Height = int(input("please enter the height of the rectangle"))
#         Area_Rectangle = Width * Height
#         print (f"the area of the rectangle is {Area_Rectangle}")
#     elif userinput == ("B").lower():
#        radius = int(input("please enter the radius of the circle"))
#        pi = 3.14159
#        Area_Circle = pi * (radius ** 2)
#        print (f"the area of the circle is {Area_Circle}")
#     elif userinput.lower() == ("C").lower():
#         Number = int(input("Please enter a number between 1,10"))
#         for i in range(1,11):
#             Times_table = Number * i
#             print (f"the multiplication table for this number is {Times_table}")
#     elif userinput == ("D").lower():
#         Num_1 = int(input("please enter a number"))
#         Num_2 = int(input("please enter a number"))
#         Num_3 = int(input("please enter a number"))
#         result = (Num_1 + Num_2 + Num_3) / 3
#         print (f"the mean of the numbers  is {result}")
#     elif userinput not in str(["A","B","C","D"]):
#         print ("Sorry, your input was not recognised, please enter either A,B,C or D")
# finished



def assessment_4():
     CoordinateX = int(input("please enter a coordinate between 1 and 10"))
     CoordinateY = int(input("please enter a coordinate between 1 and 10"))
     coordinates = CoordinateX * CoordinateY
     i = 0
     for row in range (1,11):
         for col in range(1,11):
            print("-", end="")
            if coordinates == row and col:
                print("X")
         print()



# for i in range(1,101):
    #     if i == 10:
    #         print("-,\n")
    #     for d in range (0,11):
    #         print("-",end="")


# def assessment_5():
#     #pain fix later
#     mathList = []
#     user_Input = input("please enter a choice from thee menu\nA-add numbers\nB-Display all values\nC-Replace one number\nD-Calculate the mean")
#     if user_Input == "A":
#         mathList.insert()
#         for x in mathList:
#                 print(mathList[x])





# def assessment_6():
    #     arr = [6, 5, 3, 1, 2]
    #     arr.sort()
    #     arr[0] = 67
    #     arr[1] = 69
    #     arr[2] = 71
    #     arr[3] = 72
    #     arr[4] = 73
    #     temp_value = arr[0]
    #     for r in range(len(arr)):
    #         print(arr[0], arr[r], arr[r + 1])
    #     if arr[r] > temp_value:
    #      arr[r] = temp_value

    # one of these works


    # arr = [6, 5, 3, 1, 2]
    #
    # for r in range(len(arr)):
    #     print (arr)
    #     arr[0] , arr[r] = arr[r] , arr[0]
    # print (arr)
    # print (f"the value stored in arr[0] is {arr[0]}")
    # this one somehow works
    #




# def assessment_7():
#     raise NotImplementedError("Assessment 7 has not been attempted")


if __name__ == "__main__":
    # Uncomment one of the lines below to test that assessment
    
    # print(assessment_1())
    # print(assessment_2())
    # print(assessment_3())
    print(assessment_4())
    # print(assessment_5())
    # print(assessment_6())
    # print(assessment_7())