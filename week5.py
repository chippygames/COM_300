
# is_student = "yes"
# is_notstudent = "no"
# Age = int(input(" please enter Age: "))
# if Age <= 12: print ("children under 12 get a child ticket ")
# elif Age >= 12: print ('standard ticket available!')
#
# if Age >=12: awnser = input(print("are you a student\nplease enter yes or no:"))
# if awnser == "yes" or awnser == "Yes":
#     print ("you are eligible for a discounted ticket")
# else:
#     print ("you are not eligible for a discounted ticket")

is_booked = "no"
capacity = 30

# Outer if statement
if is_booked == "no":
    # Inner if statement
    num_students = int(input("How many student?"))
    computers = input("are computers required please enter yes or no:")
    if computers.lower() == "yes":
        num_computers = int(input("how many computers are needed?"))

    else:

        if num_students <= capacity:
            percentage = 90 * (capacity/100)
            if num_students > percentage:
                print("this room is suitable however be aware of fire hazards")
            else:
                print("The room is suitable")
        else:
            print("Sorry, the room is too small")
else:
    print("This room is already booked")

# limit = 90 * (capacity/100)