# python runner.py kasle_bot.py dummybot.py

import random

#first_row[0] = "A1" = (0 0)
#first_row[1] = "B1" = (0 1)
#first_row[2] = "C1" = (0 2)
#second_row[0] = "A2" = (1 0)
#second_row[1] = "B2" = (1 1)
#second_row[2] = "C2" = (1 2)
#third_row[0] = "A3" = (2 0)
#third_row[1] = "B3" = (2 1)
#third_row[2] = "C3" = (2 2)

#BOARD =
    #['A1', 'B1', 'C1'],
    #['A2', 'B2', 'C2'],
    #['A3', 'B3', 'C3'],


class Bot:

    def board(self):
        self.me = input()
        if self.me == "X":
            self.opponent = "O"
        else:
            self.opponent = "X"
        self.first_row = input()
        self.second_row = input()
        self.third_row = input()
        self.game_board = self.create_board(self.first_row, self.second_row, self.third_row)
        return self.game_board

    def create_board(self, first_row, second_row, third_row):
        return [self.first_row, self.second_row, self.third_row]

    def make_original_move(self,x,y):
        print("{} {}".format(x, y))

    def make_move(self):
        counter = 0
        while counter < 1:
            x = random.randint(0,2)
            y = random.randint(0,2)
            z = self.game_board[x][y]
            if z != "X" and z != "O":
                print(("{} {}".format(x, y)))
                counter = 1
            else:
                counter = 0

x = Bot()
x.board()
x.make_move()
#can always be print function, or combine x and y
# print(("{} {}".format(x, y)))
