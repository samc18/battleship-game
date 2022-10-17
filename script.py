from boards import create_board, print_board
from computer import Computer
from player import Player

# DATA
ships_lengths = [2, 3, 4, 5]
valid_columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
valid_rows = ["1", "2", "3", "4", "5", "6", "7", "8"]

# BOARDS
board_player = create_board()
board_computer_hidden = create_board()
board_computer_displayed = create_board()

# INSTANCES
computer = Computer()
player = Player()

# FUNCTIONS
def validate_block(message):
    while True:
        print(message)
        block = input()
        if len(block) >= 2:
            column = block[0]
            row = block[1]
            if len(block) == 2 and column in valid_columns and row in valid_rows:
                break
            else:
                print("Please enter a valid block!")
        else:
            print("Please enter a valid block!")
    return block

def setup_player_board():
    print("-----------------------------------------------------------------------------------------")
    print("Let's start by setting your ships!")
    print("You have 4 ships, their sizes in blocks are 2, 3, 4 and 5! Set them out the best you can!")
    print("In order to setup a ship you will need to type the start block and the end block!")
    print("Here is how the board will look like so you have an idea!")
    print_board(board_player)
        
    for length in ships_lengths:
        while True:
            message_start_block = "Let's set up the {len} block long ship, type the starting block!".format(len=str(length))
            starting_block = validate_block(message_start_block)

            message_finish_block = "Type the finishing block!"
            finishing_block = validate_block(message_finish_block)

            if starting_block[0] == finishing_block[0]:
                if abs(valid_rows.index(finishing_block[1]) - valid_rows.index(starting_block[1])) == length - 1:
                    break
            elif starting_block[1] == finishing_block[1]:
                if abs(valid_columns.index(finishing_block[0]) - valid_columns.index(starting_block[0])) == length - 1:
                    break
            else:
                print("Ships can only go either horizontally or vertically!")
            
            print("Please select {len} blocks!".format(len=str(length)))

        print("{len} block ship position is {start}:{finish}".format(len=str(length), start=starting_block, finish=finishing_block))
        player.position_ship(str(starting_block), str(finishing_block), board_player)

def setup_boards():
    setup_player_board()
    computer.position_ship(2, board_computer_hidden)
    computer.position_ship(3, board_computer_hidden)
    computer.position_ship(4, board_computer_hidden)
    computer.position_ship(5, board_computer_hidden)

def display_boards():
    print_board(board_computer_displayed)
    print(" -  -  -  -  -  -  -  -  -")
    print_board(board_player)

def check_blocks_left(board):
    blocks_left = 0
    for square in board:
        for sub_square in square:
            if sub_square == "|O|":
                blocks_left += 1
    return blocks_left

def start_shooting():
    print("Let's start shooting!")

    while check_blocks_left(board_computer_hidden) != 0 or check_blocks_left(board_player) != 0:
        message_to_start_shooting = "Type where you want to shoot, for example: A1"
        block_to_be_shot = validate_block(message_to_start_shooting)
        
        player.shoot(block_to_be_shot, board_computer_hidden, board_computer_displayed)
        computer.shoot(board_player)

        display_boards()

        if check_blocks_left(board_player) == 0:
            print("The computer has won!")
            break
        elif check_blocks_left(board_computer_hidden) == 0:
            print("You have won!")
            break

def start_game():
    print("Welcome to the battleship game!")
    while True:
        print("Ready to start playing? (Y/N)")
        answer = input()
        if answer == "Y":
            setup_boards()
            display_boards()
            start_shooting()
            break
        elif answer == "N":
            print("You are missing out! Bye!")
            break
        print("Please enter a valid response, either 'Y' for yes or 'N' for no!")

# RUN GAME
start_game()