import random

class Computer:
    def position_ship(self, ship_size, board):
        row_start = random.randint(0, 7)
        column_start = random.randint(1, 8)
        
        while row_start > 7 - ship_size + 1 or column_start > 8 - ship_size + 1:
            row_start = random.randint(0, 7)
            column_start = random.randint(1, 8)
            if row_start <= 7 - ship_size + 1 or column_start <= 8 - ship_size + 1:
                break
        
        if row_start <= 7 - ship_size + 1 and column_start <= 8 - ship_size + 1:
            direction = random.randint(0, 1)
            # COLUMN = 0 | ROW = 1
            if direction == 0:
                for i in range(row_start, row_start + ship_size, 1):
                    board[i][column_start] = "|O|"
            elif direction == 1:
                for i in range(column_start, column_start + ship_size, 1):
                    board[row_start][i] = "|O|"  
        elif column_start > row_start:
            for i in range(row_start, row_start + ship_size, 1):
                board[i][column_start] = "|O|"
        elif row_start > column_start:
            for i in range(column_start, column_start + ship_size, 1):
                board[row_start][i] = "|O|"

    def shoot(self, board_player):
        row = random.randint(0, 7)
        column = random.randint(1, 8)

        while board_player[row][column] == "|-|":
            row = random.randint(0, 7)
            column = random.randint(1, 8)

        if board_player[row][column] == "|O|":
            board_player[row][column] = "|X|"
        elif board_player[row][column] == "|X|":
            board_player[row][column] = "|X|"
        else:
            board_player[row][column] = "|-|"