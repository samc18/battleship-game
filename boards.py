def create_board():
    board = [["| |"] * 8 for i in range(8)]
    number = 0
    for lst in board:
        number += 1
        lst.insert(0, str(number) + " ")
    board.append(["  ", " A ", " B ", " C ", " D ", " E ", " F ", " G ", " H "])
    return board

def print_board(board):
    for i in board:
        print("".join(i))