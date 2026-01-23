from asyncio import current_task

print ("hello world")
print ("___________\n| o o |\n| ----- |\n-------------  ")

age = 20
year = 2005
total = age + year

first_number = 200
second_number = 300

total = first_number + second_number
print (total)

price = 0.9
quantity = 30
total_price = price * quantity

print (f"You bought {quantity} things for {price}. That costs ${total_price}")


current_year = int(input ("please enter current year"))



age1 = int(input ("please enter your age"))
if age1 > 0:
    print ("your age is", age1)
    dob = current_year - age1
    print (f"{dob}")
