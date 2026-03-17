# from docutils.nodes import title
#
# city = ["england", "Southampton", 1000000]
#
# print(f"{city[1]} is in {city[0]} and has a population of {city[2]}")
#
# stastic = {
#     "Country": "england",
#     "City":"Southampton",
#     "population": 1000000
# }
#
# print(f"{stastic['City']} is in {stastic['Country']} and has a population of {stastic['population']}")
#
#
#
# my_string = "fghhdgfdhghfdhbfdfhdsvbfdhvlhhkbfxhbkxhjlbhjjkcbfghjhvc"
#
# counts = {}
#
# for char in my_string:
#     if char in counts:
#         counts[char] += 1
#     else:
#         counts[char] = 1
#
# for letter, count in counts.items():
#     print(f"{letter} appears {count} times")
#
def greeting():

    game = {

        "title": "Pokemon alpha saphire",
        "publisher": 'Gamefreak',
        'year':2014
    }
    print (f"the game {game["title"]} was made by {game['publisher']} in the year {game['year']}  ")

    info = input("would you like to know more information about this game?")
    data = input("please enter your data")

    game[info] = data

    print (game)

greeting()
