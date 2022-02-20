import random

def main():
    words = read_words('words.txt')
    word = words[random.randint(0, len(words) - 1)]

    tries = 6
    correct = [2, 2, 2, 2, 2]

    game_won = False

    while tries != 0:
        guess = take_guess(words)
        formatted_guess = check_guess(guess, word)
        print(format_guess(formatted_guess, guess))
        tries -= 1
        if formatted_guess == correct:
            game_won = True
            tries = 0
    

    if game_won:
        print('You won')
    else:
        print('You lost')


def read_words(file):
    word_str = ''
    word_lst = []

    with open(file) as f:
        word_str = f.read()
    word_lst = word_str.split('\n')

    return word_lst


def take_guess(allowed_gueses):
    guess = str(input())
    guess = guess.lower()

    if guess not in allowed_gueses:
        take_guess(allowed_gueses)
    else:
        return guess


def check_guess(guess, real_word):
    how_close = []
    any_letters_in_word = False

    for i in range(5):
        for j in range(5):
            if guess[i] == real_word[j]:
                any_letters_in_word = True
        if guess[i] == real_word[i]:
            how_close.append(2)
        elif any_letters_in_word:
            how_close.append(1)
        else:
            how_close.append(0)
            
    return how_close


def format_guess(closeness, word):
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    reset = '\u001b[0m'
    format_buffer = ''

    for i in range(5):
        if closeness[i] == 2:
            format_buffer += green + word[i]
        elif closeness[i] == 1:
            format_buffer += yellow + word[i]
        else:
            format_buffer += reset + word[i]
        
        format_buffer += reset
        
    return format_buffer


if __name__ == '__main__':
    main()