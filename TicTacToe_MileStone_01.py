# Imports
import random
import os


def user_input(player):
    """
    This will grab the user input and make sure that it is appropriate
    Both values have to be true to return the
    """
    acceptable_numbers = list(range(1, 10))
    guess_is_number = False
    guess_is_valid = False
    def_player_guess = ""
    while guess_is_number is False or guess_is_valid is False:
        def_player_guess = input(f"{player} please enter a value of 1 to 9: ")
        if def_player_guess.isdigit():
            guess_is_number = True
            if int(def_player_guess) in acceptable_numbers:
                guess_is_valid = True
            else:
                guess_is_valid = False
                print(f"{player} please input a number from 1 to 9.")
        else:
            guess_is_number = False
            print(f"{player} please input a number from 1 to 9.")
    return int(def_player_guess)


def player_setup(def_first_player):
    """
    This will set up the players for X or O.  Player 1 picks and player 2 is automatic
    """
    player_option = ""
    player_list = []
    player_input = False
    while player_input is False:
        player_option = input(f"{def_first_player} please select X or O for your character: ").upper()
        if player_option.upper() == "X" or player_option.upper() == "O":
            player_input = True
            print(f"{def_first_player} is playing as {player_option}")
        else:
            print("Please select either X or O as options.")
            player_input = False
    if def_first_player == "Player 1":
        if player_option.upper() == "X":
            print("Player 2 is playing as O")
            player_list.append("X")
            player_list.append("O")
        elif player_option.upper() == "O":
            print("Player 2 is playing as X")
            player_list.append("O")
            player_list.append("X")
    elif def_first_player == "Player 2":
        if player_option.upper() == "X":
            print("Player 1 is playing as O")
            player_list.append("O")
            player_list.append("X")
        elif player_option.upper() == "O":
            print("Player 1 is playing as X")
            player_list.append("O")
            player_list.append("X")
    return player_list[0], player_list[1]


def board_setup(board_numbers):
    print("   |   |   ")
    print(f" {board_numbers[1]} | {board_numbers[2]} | {board_numbers[3]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board_numbers[4]} | {board_numbers[5]} | {board_numbers[6]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board_numbers[7]} | {board_numbers[8]} | {board_numbers[9]} ")
    print("   |   |   ")


def choose_player():
    """
    This will randomly choose a player based on 1 or 0
    """
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"


def check_if_full(board_to_check):
    """
    will check to see if any pieces are available to play
    after last play
    """
    for item in range(1, 10):
        if board_to_check[item] in range(1, 10):
            return True
    return False


def replay_game():
    """
    Ask the user if they want to game more
    """
    while True:
        player_option = input("Do you want to play again? (Y or N): ").upper()
        if player_option.upper() == "Y":
            return True
        elif player_option.upper() == "N":
            return False
        else:
            print("Please select either Y or N as options.")


def check_win(board_to_check, mark, player):
    """
    Check to see if they won
    """
    winning_player = player.upper()
    # top row
    if board_to_check[1] == board_to_check[2] == board_to_check[3] == mark:
        clear()
        print(f"{winning_player} WON MATCHING THE TOP ROW!!!!!")
        board_setup(board_to_check)
        return True
    # middle row
    elif board_to_check[4] == board_to_check[5] == board_to_check[6] == mark:
        clear()
        print(f"{winning_player} WON MATCHING THE MIDDLE ROW!!!!!")
        board_setup(board_to_check)
        return True
    # bottom row
    elif board_to_check[7] == board_to_check[8] == board_to_check[9] == mark:
        clear()
        print(f"{winning_player} WON MATCHING THE BOTTOM ROW!!!!!")
        board_setup(board_to_check)
        return True
    # left column
    elif board_to_check[1] == board_to_check[4] == board_to_check[7] == mark:
        clear()
        print(f"{winning_player} WON MATCHING THE LEFT COLUMN!!!!!")
        board_setup(board_to_check)
        return True
    # middle column
    elif board_to_check[2] == board_to_check[5] == board_to_check[8] == mark:
        clear()
        print(f"{winning_player} WON MATCHING THE MIDDLE COLUMN!!!!!")
        board_setup(board_to_check)
        return True
    # right column
    elif board_to_check[3] == board_to_check[6] == board_to_check[9] == mark:
        clear()
        print(f"{winning_player} WON MATCHING THE RIGHT COLUMN!!!!!")
        board_setup(board_to_check)
        return True
    # left to right diagonal
    elif board_to_check[1] == board_to_check[5] == board_to_check[9] == mark:
        clear()
        print(f"{winning_player} WON MATCHING THE RIGHT DIAGONAL!!!!!")
        board_setup(board_to_check)
        return True
    # right to left diagonal
    elif board_to_check[3] == board_to_check[5] == board_to_check[7] == mark:
        clear()
        print(f"{winning_player} WON MATCHING THE LEFT DIAGONAL!!!!!")
        board_setup(board_to_check)
        return True
    else:
        return False


def clear():
    os.system('cls')


print("Welcome to Tic Tac Toe!!!")
continue_gaming = True
clear()
while continue_gaming:
    first_player = choose_player()
    player_1_character, player_2_character = player_setup(first_player)
    board_pieces = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    current_player = first_player
    game_continues = True
    player_mark = ""
    while game_continues:
        clear()
        board_setup(board_pieces)
        player_pick = True
        while player_pick:
            player_guess = user_input(current_player)
            for index in range(1, 10):
                if player_guess == board_pieces[index]:
                    if current_player == "Player 1":
                        board_pieces[index] = player_1_character
                        player_pick = False
                        player_mark = player_1_character
                    elif current_player == "Player 2":
                        board_pieces[index] = player_2_character
                        player_pick = False
                        player_mark = player_2_character
            if player_pick:
                print("Pick a free option!!")
        win_yes_no = check_win(board_pieces, player_mark, current_player)
        if win_yes_no:
            game_continues = False
        full_yes_no = check_if_full(board_pieces)
        if not full_yes_no:
            print("Board is full.  Thank you for playing.")
            game_continues = False
        if current_player == "Player 1":
            current_player = "Player 2"
        elif current_player == "Player 2":
            current_player = "Player 1"
    print("Thank you for playing.")
    continue_gaming = replay_game()
print("Thank you for playing")
