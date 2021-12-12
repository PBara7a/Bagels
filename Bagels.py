"""Bagels, by Paulo Barata.
A deductive logic game where you must guess a number based on clues.
This is based on Al Sweigart's version on The Big Book of Small Python Projects.
12/2021"""

import random


def main():
    print(f'''Bagels, a deductive logic game. By Paulo Barata.

I will think of a {num_digits}-digit number with no repeated digits.
You try to guess what number it is. The clues are:
If I say:       That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.

Example: If the secret number was 248 and your guess was 843, the clues would be Fermi Pico.''')

    while True:  # Main game loop
        secret_num = get_secret_num()
        print('I have thougth of a number.')
        print(f'You have {max_guesses} guesses to get it.')

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            # Loops until the guess is valid
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Guess #{num_guesses}: ')
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses =+ 1

            if guess == secret_num:
                break  # Its a win -> break loop
            if num_guesses > max_guesses:
                print('You ran out of guesses.')
                print(f'The answer was {secret_num}.')

        # Ask player for another round
        print('Do you want to play again? (y/n)')
        if not input('> ').lower() == 'y':
            break # Stop playing
    print('Thanks for playing!')

def get_secret_num():
    """Returns a string with num_digits unique random digits."""
    numbers = list('0123456789')  # Initialise list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffles list of digits randomly.

    # Get the first num_digits digits in the list for the secret number:
    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num

def get_clues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secret_num:
        return 'Congrats! You guessed it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits.
    else:
        # Sort the clues in alphabetical order so their original order doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)

def get_num_digits():
    num = 'a'
    while not num.isdecimal():
        num = input('How many digits can you handle? (max: 10)> ')
    return int(num)

def get_max_guesses():
    max = 'a'
    while not max.isdecimal():
        max = input('How many guesses do you think you need?> ')
    return int(max)

num_digits = get_num_digits()
max_guesses = get_max_guesses()

if __name__ == '__main__':
    main()
