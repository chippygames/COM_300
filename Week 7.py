# Numbers = [0,1,26,30,89]
# for c in range(len(Numbers)):
#     print(Numbers[c])
# user_element = int(input("please enter a new element number"))
# new_value = int(input("please enter a new value "))
# Numbers[user_element] = new_value
# for c in range(len(Numbers)):
#     print(Numbers[c])
from fontTools.misc.cython import returns




Results = []
Letter = []
for i in range(5):
    new_letter = input("Enter letter: ")
    Letter.append(new_letter)
    new_useresult = int(input("Enter new results: "))
    Results.append(new_useresult)

for c in range(len(Results)):

    print (f"the result of experiment {Letter[c]} is {Results[c]}")





