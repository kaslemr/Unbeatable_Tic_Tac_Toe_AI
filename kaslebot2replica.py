#1st python runner.py kaslebot2replica.py kaslebot2.py
#2nd python runner.py kaslebot2.py kaslebot2replica.py

#1st python runner.py kaslebot2.py player
#2nd python runner.py player kaslebot2.py

import random

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
        self.first_column = self.create_column(0, 0, 0)
        self.second_column = self.create_column(1, 1, 1)
        self.third_column = self.create_column(2, 2, 2)
        self.left_right_diagonal = self.create_column(0, 1, 2)
        self.right_left_diagonal = self.create_column(2, 1, 0)
        self.corners = self.first_row[0], self.first_row[2], self.third_row[0], self.third_row[2]
        self.positions = [item for sublist in self.game_board for item in sublist]
        self.positions_taken = self.positions.count("X") + self.positions.count("O")
        return self.game_board

    def create_board(self, first_row, second_row, third_row):
        return [self.first_row, self.second_row, self.third_row]

    def create_column(self, x, y, z):
        return [self.first_row[x], self.second_row[y], self.third_row[z]]

    def make_original_move(self,x,y):
        print("{} {}".format(x, y))

    def make_move(self):
        counter = 0
        while counter < 0.5:
            if self.first_move() != False:
                counter = 1
            elif self.get_win() != False:
                counter = 1
            elif self.block_win() != False:
                counter = 1
            elif self.second_move() != False:
                counter = 1
            else:
                if self.corners.count("_") < 4:
                    x = random.choice([0, 2])
                    y = random.choice([0, 2])
                    if z != "X" and z != "O":
                        print(("{} {}".format(x, y)))
                        counter = 1
                    else:
                        counter = 0
                elif:
                    x = random.randint(0,2)
                    y = random.randint(0,2)
                    z = self.game_board[x][y]
                    if z != "X" and z != "O":
                        print(("{} {}".format(x, y)))
                        counter = 1
                    else:
                        counter = 0

    def first_move(self):
        if self.me not in self.first_row and self.me not in self.second_row and self.me not in self.third_row:
            if self.opponent in self.first_row or self.opponent in self.second_row or self.opponent in self.third_row:
                if self.opponent in self.corners:
                    print(1,1)
                else:
                    print(0,0)
            else:
                print(0,0)
        else:
            return False

    def second_move(self):
        if self.positions_taken == 2:
            if self.second_row[1] == self.opponent:
                print(2,2)
                counter = 1
            else:
                return False
        elif self.positions_taken == 3:
            if self.corners.count(self.opponent) == 2:
                x = 1
                y = random.choice([0, 2])
                z = self.game_board[x][y]
                if z != "X" and z != "O":
                    print(("{} {}".format(x, y)))
                    counter = 1
                else:
                    return False
            else:
                return False
        else:
            return False

    def block_win(self):
        if self.first_row.count(self.opponent) == 2 and self.first_row.count("_") == 1:
            y = self.first_row.index("_")
            print(0, y)
        elif self.second_row.count(self.opponent) == 2 and self.second_row.count('_') == 1:
            y = self.second_row.index("_")
            print(1, y)
        elif self.third_row.count(self.opponent) == 2 and self.third_row.count("_") == 1:
            y = self.third_row.index("_")
            print(2, y)
        elif self.first_column.count(self.opponent) == 2 and self.first_column.count("_") == 1:
            x = self.first_column.index("_")
            print(x, 0)
        elif self.second_column.count(self.opponent) == 2 and self.second_column.count("_") == 1:
            x = self.second_column.index("_")
            print(x, 1)
        elif self.third_column.count(self.opponent) == 2 and self.third_column.count("_") == 1:
            x = self.third_column.index("_")
            print(x, 2)
        elif self.left_right_diagonal.count(self.opponent) == 2 and self.left_right_diagonal.count("_") == 1:
            x = self.left_right_diagonal.index("_")
            if x == 0:
                y = 0
            if x == 1:
                y = 1
            if x == 2:
                y = 2
            print(x, y)
        elif self.right_left_diagonal.count(self.opponent) == 2 and self.right_left_diagonal.count("_") == 1:
            x = self.right_left_diagonal.index("_")
            if x == 0:
                y = 2
            if x == 1:
                y = 1
            if x == 2:
                y = 0
            print(x, y)
        else:
            return False

    def get_win(self):
        if self.first_row.count(self.me) == 2 and self.first_row.count("_") == 1:
            y = self.first_row.index("_")
            print(0, y)
        elif self.second_row.count(self.me) == 2 and self.second_row.count("_") == 1:
            y = self.second_row.index("_")
            print(1, y)
        elif self.third_row.count(self.me) == 2 and self.third_row.count("_") == 1:
            y = self.third_row.index("_")
            print(2, y)
        elif self.first_column.count(self.me) == 2 and self.first_column.count("_") == 1:
            x = self.first_column.index("_")
            print(x, 0)
        elif self.second_column.count(self.me) == 2 and self.second_column.count("_") == 1:
            x = self.second_column.index("_")
            print(x, 1)
        elif self.third_column.count(self.me) == 2 and self.third_column.count("_") == 1:
            x = self.third_column.index("_")
            print(x, 2)
        elif self.left_right_diagonal.count(self.me) == 2 and self.left_right_diagonal.count("_") == 1:
            x = self.left_right_diagonal.index("_")
            if x == 0:
                y = 0
            if x == 1:
                y = 1
            if x == 2:
                y = 2
            print(x, y)
        elif self.right_left_diagonal.count(self.opponent) == 2 and self.right_left_diagonal.count("_") == 1:
            x = self.right_left_diagonal.index("_")
            if x == 0:
                y = 2
            if x == 1:
                y = 1
            if x == 2:
                y = 0
            print(x, y)
        else:
            return False

x = Bot()
x.board()
x.make_move()
