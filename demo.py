
for row in range(1, 4): # [1, 2, 3]
    for num in range(1, 4):     # [1, 2, 3]
        answer = num * row
        print(answer, end="\t")
    print()



row = 2
num = 2
answer = 4
"""
1   2   3   
2   4   

"""



is_booked = "no"
capacity = 30

# Outer if statement
if is_booked == "no":
    # Inner if statement
    num_students = int(input("How many student?"))
    if num_students <= capacity:
        print("The room is suitable")
    else:
        print("Sorry, the room is too small")
else:
    print("This room is already booked")


def random_func():
