class Player:
    letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

    def position_ship(self, start_pos, finish_pos, board):
        # START
        letter_start = start_pos[0]
        number_start = start_pos[1]
        row_start = int(number_start) - 1
        column_start = self.letters_to_numbers[letter_start] + 1

        # FINISH
        letter_finish = finish_pos[0]
        number_finish = finish_pos[1]
        row_finish = int(number_finish) - 1
        column_finish = self.letters_to_numbers[letter_finish] + 1

        new_row_start = min(row_start, row_finish)
        new_row_finish = max(row_start, row_finish)
        new_column_start = min(column_start, column_finish)
        new_column_finish = max(column_start, column_finish)

        if letter_start == letter_finish:
            for i in range(new_row_start, new_row_finish + 1, 1):
                board[i][column_start] = "|O|"
            
        elif row_start == row_finish:
            for i in range(new_column_start, new_column_finish + 1, 1):
                board[row_start][i] = "|O|"

    def shoot(self, position, board_computer_hidden, board_computer_displayed):
        letter = position[0]
        number = position[1]
        row = int(number) - 1
        column = self.letters_to_numbers[letter] + 1

        if board_computer_hidden[row][column] == "|O|":
            board_computer_hidden[row][column] = "|X|"
            board_computer_displayed[row][column] = "|X|"
        elif board_computer_hidden[row][column] == "|X|":
            board_computer_hidden[row][column] = "|X|"
            board_computer_displayed[row][column] = "|X|"
        else:
            board_computer_hidden[row][column] = "|-|"
            board_computer_displayed[row][column] = "|-|"