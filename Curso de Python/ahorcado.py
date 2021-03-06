import random

IMAGES = ['''
            +---+
            |   |
                |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            /|   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            /|\  |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            /|\  |
            /    |
                |
            =========''', '''
            +---+
            |   |
            O   |
            /|\  |
            / \  |
                |
            =========''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]


def random_word():
    idx = random.randint(0, len(WORDS) -1)
    return WORDS[idx]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('---*'*5)


def run():
    print('BIENVENIDOS A AHORCADOS')
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = input('Escoge una letra: ')

        letter_index = letter_appear(word, current_letter)

        if len(letter_index) == 0:
            tries += 1
            if tries == 6:
                display_board(hidden_word, tries)
                print('You Lose! The Secret Words was:{}'.format(word))
                break
        else:
            print(letter_index)
            for idx in letter_index:
                hidden_word[idx] = current_letter

            letter_index = []
        try:
            hidden_word.index('-')
        except ValueError:
            print('You Win! The Secret Words was:{}'.format(word))
            break

def letter_appear(word, current_letter):
    letter_index = []
    for idx in range(len(word)):
        if word[idx] == current_letter:
            letter_index.append(idx)
    return letter_index

if __name__ == "__main__":
    run()