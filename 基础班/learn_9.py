
import random


count = 1000

three_door = [1, 2, 3]
no_change_win = 0
change_win = 0


# for i in range(count):
#     award = random.choice(three_door)
#     choice = random.choice(three_door)
#     if choice == award:
#         no_change_win += 1

# print(no_change_win / count)

for i in range(count):
    award = random.choice(three_door)
    choice = random.choice(three_door)
    if choice == award:
        temp = three_door.copy()
        temp.remove(choice)
        close = random.choice(temp)
    else:
        change_win += 1

    # temp = three_door.copy()
    # temp.remove(choice)
    # temp.remove(award)
    # close = temp[0]
    # temp_1 = three_door.copy()
    # temp_1.remove(choice)
    # temp_1.remove(close)
    # change_choice = temp_1[0]
    # if change_choice == award:
    #     change_win += 1

print(change_win / count)
