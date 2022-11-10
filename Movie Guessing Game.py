# Bollywood Movie Guessing Game

from collections import Counter
import pwinput

while True:
    print('_______________________Movie Guessing Game_______________________\n')

    word = pwinput.pwinput(prompt='Enter your Movie: ', mask='*')

    if word == 'end':
        break

    if ' ' not in word:
        correct = 0
        for i in word:
            print('_', end=' ')
    else:
        correct = -1

    chance = 10

    flag = 0
    letter = ''
    full_word = ''
    wrong_word = ''

    for l in word:
        full_word = full_word + l + ' '

    while (chance != 0) and flag == 0:

        if (chance == 10) and (' ' not in word):
            print('\nChances left... ', chance)

        if (correct == -1) and (' ' in word):
            guess = ' '
            chance = chance + 1
        else:
            guess = str(input('\nEnter you guessed alphabet: '))

        if guess in letter:
            print('\nYou have already guessed that letter')
            chance = chance + 1
            continue

        elif guess in wrong_word:
            print('\nYou have already guessed that letter')
            chance = chance + 1
            continue

        elif guess == word:
            print('\nYou Guessed just in time: ', full_word)
            print('\n__________________ YOU WON THE GAME_____________________\n\n')
            break

        elif not (len(guess) == 1):
            print('Enter only a SINGLE letter')
            chance = chance + 1
            continue

        if guess in word:
            k = word.count(guess)
            for i in range(0, k):
                letter = letter + guess
        else:
            wrong_word = wrong_word + guess

        chance = chance - 1

        for char in word:

            if (char in letter) and (Counter(letter) != Counter(word)):
                print(char, end=' ')
                correct = correct + 1

            elif (Counter(letter) == Counter(word)):
                print('\nYou Guessed just in time: ', full_word)
                print('\n__________________ YOU WON THE GAME_____________________\n\n')
                flag = 1
                break
                break

            else:
                print('_', end=' ')

        if (Counter(letter) == Counter(word)) or (guess == word):
            break
        else:
            print('\nChances left... ', chance)

        if chance <= 0 and (Counter(letter) != Counter(word)):
            print('\n___________________YOU LOST THE GAME :(_____________________')
            print('The original word was:  ', full_word, '\n\n')
