
# Imports
import random
import os

def guess_check(letter_guessed):
    '''
    This will check the letter passed to it and see if 
	it has already been guessed.  If it has, it 
	will then repeat until the user guesses a 
	non-guessed letter.
	'''
    already_guessed = True
    while already_guessed:
        if dict_letter_options[letter_guessed] == 0:
            print("You already guessed that letter.  Please try again.")
            letter_guessed = str(input("Please enter your guess (-1 to exit): "))
            if letter_guessed == "-1":
                print("Thank you for playing!!")
                exit()
            elif dict_letter_options[letter_guessed] == 1:
                dict_letter_options[letter_guessed] = 0
                already_guessed = False
	

# The main part of the script
if __name__ == "__main__":
    words = ('Pam', 'Jim', 'Dwight', 'Kevin', 'Creed')
    randomNumber = random.randint(0, (len(words) - 1))
    wordToUse = words[randomNumber]
    continuePlaying = True
    you_Lose = False
    correct_Guess = False
    wrong_guesses = 0
    clear = lambda: os.system('cls')
    dict_letter_options = {'a' : 1, 'b' : 1, 'c' : 1, 'd' : 1, 'e' : 1,
                           'f' : 1, 'g' : 1, 'h' : 1, 'i' : 1, 'j' : 1,
                           'k' : 1, 'l' : 1, 'm' : 1, 'n' : 1, 'o' : 1,
                           'p' : 1, 'w' : 1, 'r' : 1, 's' : 1, 't' : 1,
                           'u' : 1, 'v' : 1, 'w' : 1, 'x' : 1, 'y' : 1,
                           'z' : 1,}
    clear()
    print("Welcome to Hangman!!!!")
    print("This is your first time playing I see")
    print("Let's begin")
    print("\nLetter Options include:\n")
    for letters in dict_letter_options.keys():
        print(f"{letters} ", end='')
    print("")
    print("   ___")
    print("  |   |")
    for x in range(0,6):
        print("      |")
        x += 1
    print("    __|__")
    print("\n\n")
    blank_length = "_ " * (len(wordToUse))
    print(blank_length)
    word_key_list = []
    answer_list = []
    for x in range(0, (len(wordToUse))):
        word_key_list.append(wordToUse[x])
        answer_list.append('_')
    roundOfPlay = 0
    while continuePlaying:
        player_input = str(input("Please enter your guess (-1 to exit): "))
        player_guess = player_input.lower()
        if player_guess == "-1":
            print("Thank you for playing!!")
            exit()
        correct_answer = False
        for answer_index in range(0,(len(word_key_list))):
            if player_guess.upper() == word_key_list[answer_index].upper():
                answer_list[answer_index] = player_guess.upper()
                correct_answer = True
                are_all_answered = 0
                for letter in answer_list:
                    if letter != '_':
                        are_all_answered += 1
                if are_all_answered == len(answer_list):
                    continuePlaying = False
                    you_Lose = False
        if correct_answer is False:
            roundOfPlay = roundOfPlay + 1
        all_letters_guessed = False
        for letters in dict_letter_options.keys():
            if dict_letter_options[letters] == 1:
                all_letters_guessed = True
        if all_letters_guessed is False:
            continuePlaying = False
        elif roundOfPlay >= 7:
            continuePlaying = False
            you_Lose = True
        elif roundOfPlay == 6:
            clear()
            print("\nLetter Options include:\n")
            for letters in dict_letter_options.keys():
                if dict_letter_options[letters] == 1:
                    print(f"{letters} ", end='')
                elif dict_letter_options[letters] == 0:
                    print("?? ", end='')
            print("")
            print("   ___")
            print("  |   |")
            print("  O   |")
            print(" /|\  |")
            print("  |   |")
            print(" /    |")
            print("      |")
            print("      |")
            print("    __|__")
            print("\n\n")
            for answer_key in answer_list:
                print(f"{answer_key} ", end='')
            print("")
            print("\n1 TRIES LEFT!!")
        elif roundOfPlay == 5:
            clear()
            print("\nLetter Options include:\n")
            for letters in dict_letter_options.keys():
                if dict_letter_options[letters] == 1:
                    print(f"{letters} ", end='')
                elif dict_letter_options[letters] == 0:
                    print("?? ", end='')
            print("")
            print("   ___")
            print("  |   |")
            print("  O   |")
            print(" /|\  |")
            print("  |   |")
            print("      |")
            print("      |")
            print("      |")
            print("    __|__")
            print("\n\n")
            for answer_key in answer_list:
                print(f"{answer_key} ", end='')
            print("")
            print("\n2 TRIES LEFT!!")
        elif roundOfPlay == 4:
            clear()
            print("\nLetter Options include:\n")
            for letters in dict_letter_options.keys():
                if dict_letter_options[letters] == 1:
                    print(f"{letters} ", end='')
                elif dict_letter_options[letters] == 0:
                    print("?? ", end='')
            print("")
            print("   ___")
            print("  |   |")
            print("  O   |")
            print(" /|\  |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("    __|__")
            print("\n\n")
            for answer_key in answer_list:
                print(f"{answer_key} ", end='')
            print("")
            print("\n3 TRIES LEFT!!")
        elif roundOfPlay == 3:
            clear()
            print("\nLetter Options include:\n")
            for letters in dict_letter_options.keys():
                if dict_letter_options[letters] == 1:
                    print(f"{letters} ", end='')
                elif dict_letter_options[letters] == 0:
                    print("?? ", end='')
            print("")
            print("   ___")
            print("  |   |")
            print("  O   |")
            print(" /|   |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("    __|__")
            print("\n\n")
            for answer_key in answer_list:
                print(f"{answer_key} ", end='')
            print("")
            print("\n4 TRIES LEFT!!")
        elif roundOfPlay == 2:
            clear()
            print("\nLetter Options include:\n")
            for letters in dict_letter_options.keys():
                if dict_letter_options[letters] == 1:
                    print(f"{letters} ", end='')
                elif dict_letter_options[letters] == 0:
                    print("?? ", end='')
            print("")
            print("   ___")
            print("  |   |")
            print("  O   |")
            print("  |   |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("    __|__")
            print("\n\n")
            for answer_key in answer_list:
                print(f"{answer_key} ", end='')
            print("")
            print("\n5 TRIES LEFT!!")
        elif roundOfPlay == 1:
            clear()
            print("\nLetter Options include:\n")
            for letters in dict_letter_options.keys():
                if dict_letter_options[letters] == 1:
                    print(f"{letters} ", end='')
                elif dict_letter_options[letters] == 0:
                    print("?? ", end='')
            print("")
            print("   ___")
            print("  |   |")
            print("  O   |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("    __|__")
            print("\n\n")
            for answer_key in answer_list:
                print(f"{answer_key} ", end='')
            print("")
            print("\n6 TRIES LEFT!!")
        elif roundOfPlay == 0:
            clear()
            print("\nLetter Options include:\n")
            for letters in dict_letter_options.keys():
                if dict_letter_options[letters] == 1:
                    print(f"{letters} ", end='')
                elif dict_letter_options[letters] == 0:
                    print("?? ", end='')
            print("")
            print("   ___")
            print("  |   |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("    __|__")
            print("\n\n")
            for answer_key in answer_list:
                print(f"{answer_key} ", end='')
            print("")
            print("\n7 TRIES LEFT!!")
            
    if you_Lose:
        print("\n\n")
        print("YOU LOST!!!!")
    else:
        print("\n\n")
        print("YOU WON!!!!")

