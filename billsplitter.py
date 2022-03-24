from random import choice

output = int(input("Enter the number of friends joining (including you):\n"))


def split_value(members, total, count):
    members.update({i: round(total / count, 2) for i in friends})
    return members


if output > 0:
    print("Enter the name of every friend (including you), each on a new line:\n")
    friends = dict.fromkeys([input() for _ in range(output)], 0)
    bill = int(input("Enter the total bill value:\n"))
    friends = split_value(friends, bill, len(friends))
    if input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n') == "Yes":
        friends = split_value(friends, bill, len(friends) - 1)
        lucky_friend = choice([key for key in friends])
        friends[lucky_friend] = 0
        print(f"{lucky_friend} is the lucky one!")
    else:
        print("No one is going to be lucky")
    print(friends)
else:
    print("No one is joining for the party")
