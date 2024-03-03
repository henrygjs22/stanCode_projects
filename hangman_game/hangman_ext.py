"""
File: hangman.py
Name: Henry
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7
HANGMAN = '\n\n\n'
HANGMAN1 = '  Ｏ\n\n'
HANGMAN2 = '  Ｏ\n　｜\n'
HANGMAN3 = '  Ｏ\n／｜\n'
HANGMAN4 = '  Ｏ\n／｜＼\n'
HANGMAN5 = '  Ｏ\n／｜＼\n ／'
HANGMAN6 = '  Ｏ\n／｜＼\n ／＼'
DEADMAN = '  Ｘ\n／｜＼\n ／＼'


def main():
    """
    TODO: Make hangman image of every status as constant, then make and call function
          to show hangman
    """
    answer = random_word().upper()
    dash = '–'*len(answer)
    count = 0
    print('The word looks like ' + dash)
    print(f'You have {N_TURNS} wrong guesses left.')
    while True:
        print('-'*30)
        input_ch = input('Your guess: ').upper()
        location = answer.find(input_ch)
        if len(input_ch) != 1 or not input_ch.isalpha():
            print('Illegal format.')
            continue
        if location == -1:
            count += 1
            print("There's no " + input_ch + "'s in the word.")
            if count == N_TURNS:
                print('You are completely hung ：（')
                hangman(count)
                print('The word was: ' + answer)
                break
            print('The word looks like ' + dash)
            hangman(count)
            print(f'You have {N_TURNS-count} wrong guesses left.')
        else:
            for i in range(len(answer)):
                if input_ch == answer[i]:
                    dash = dash[0:i] + input_ch + dash[i+1:]
            print('You are correct!')
            if dash == answer:
                print('You win!!')
                print('The word was: ' + answer)
                break
            print('The word looks like ' + dash)
            hangman(count)
            print(f'You have {N_TURNS-count} wrong guesses left.')


def hangman(count):
    if count == N_TURNS:
        print(DEADMAN)
    elif count == 0:
        print(HANGMAN)
    elif count == 1:
        print(HANGMAN1)
    elif count == 2:
        print(HANGMAN2)
    elif count == 3:
        print(HANGMAN3)
    elif count == 4:
        print(HANGMAN4)
    elif count == 5:
        print(HANGMAN5)
    else:
        print(HANGMAN6)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
