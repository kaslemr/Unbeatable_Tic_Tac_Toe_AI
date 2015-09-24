import random

team = input()
first_row = input()
second_row = input()
third_row = input()

board = [first_row, second_row, third_row]


counter = 0

while counter < 1:
    x = random.randint(0,2)
    y = random.randint(0,2)
    if board[x][y] == "_":
        print(("{} {}".format(x, y)))
        counter += 1
    else:
        counter = 0
