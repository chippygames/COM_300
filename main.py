


def calculate_fee(distance):
    if distance <= 10:
        return 0
    elif distance <= 10:
        return 10
    elif distance <= 20:
        return 15
    elif distance <= 30:
        return 15
    elif distance < 40:
        return 0

    return


def assessment_1():
    order_Value = int(input("please enter your order number"))
    distance = int(input("please enter your distance"))
    cost = 3.95

    deliveryfee = calculate_fee(distance)


    total_cost = cost + deliveryfee

    print(f"the total cost is  {total_cost}")
    print(f"delivery cost is {deliveryfee}")
    print(f"you are {distance} miles away")
    print(f"you paid {cost} dollars")
    return
#simple drone delivery service

def assessment_2():
    raise NotImplementedError("Assessment 2 has not been attempted")


def assessment_3():
    raise NotImplementedError("Assessment 3 has not been attempted")


def assessment_4():
    raise NotImplementedError("Assessment 4 has not been attempted")


def assessment_5():
    raise NotImplementedError("Assessment 5 has not been attempted")


def assessment_6():
    raise NotImplementedError("Assessment 6 has not been attempted")


def assessment_7():
    raise NotImplementedError("Assessment 7 has not been attempted")


if __name__ == "__main__":
    # Uncomment one of the lines below to test that assessment
    
    print(assessment_1())
    # print(assessment_2())
    # print(assessment_3())
    # print(assessment_4())
    # print(assessment_5())
    # print(assessment_6())
    # print(assessment_7())
    pass