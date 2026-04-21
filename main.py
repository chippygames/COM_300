


from Charachter import Character


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
import math
from sys import flags


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
     coordinateX = int(input("please enter a coordinate between 1 and 10"))
     coordinateY = int(input("please enter a coordinate between 1 and 10"))

     for row in range (1,11):
         for col in range(1,11):
            if coordinateY == row and coordinateX == col:
                print("X", end="")
            else:
                print("-", end="")
         print()


def assessment_5():
    # pain fix later "loop everything so it updates after all questions done
    math_List = []
    while True:
        user_Input = input("please enter a choice from the menu\nA-add numbers\nB-Display all values\nC-Replace one number\nD-Calculate the mean\nE-Find the largest number in the list\nX-Exit")


        if user_Input.lower() == "a":
            how_many =(int(input("how many numbers you would like to add\n")))
            for i in range(how_many):
                number = int(input("please enter your number"))
                math_List.append(number)
            print (math_List)

        elif user_Input.lower() == "b":
            for i in math_List:
                print(i)

        elif user_Input.lower() == "c":
            order_new = (int(input("please enter what element you would like to replace")))
            new_number = (int(input("please enter your number")))
            print (math_List[order_new])
            math_List[order_new] = new_number
            print (math_List)

        elif user_Input.lower() == "d":
            count = 0
            tally = 0
            for i in range(len(math_List)):
                tally += math_List[i]
                count += 1
            awnser = tally/count
            print(awnser)

        elif user_Input.lower() == "e":
            big_number = max(math_List)
            print(f"the largest number in the list is {big_number}")

        elif user_Input.lower() == "x":
                print("thank you for using this program")
                break

        else: user_Input.upper() == "A", "B", "C", "D", "E", "X"
        print("Please enter a valid letter from the menu.")




def assessment_6():
        # arr = [6, 5, 3, 1, 2]
        # arr.sort()
        # arr[0] = 67
        # arr[1] = 69
        # arr[2] = 71
        # arr[3] = 72
        # arr[4] = 73
        # temp_value = arr[0]
        # for r in range(len(arr)):
        #     print(arr[0], arr[r], arr[r + 1])
        # if arr[r] > temp_value:
        #  arr[r] = temp_value

    arr = [6, 5, 3, 1, 2]
    for r in range(len(arr)):
        #     print (arr)
        #     arr[0] , arr[r] = arr[r] , arr[0]
        # print (arr)
        print (f"the value stored in arr[0] is {arr[0]} and the other value is {arr[r]}")







 def assessment_7():

    player1 = Character("luke",100,50,100)
    player2 = Character("bob",100,50,100)


    player1.info()








if __name__ == "__main__":

    # print(assessment_1())
    # print(assessment_2())
    # print(assessment_3())
    # print(assessment_4())
    # print(assessment_5())
    # print(assessment_6())
    print(assessment_7())