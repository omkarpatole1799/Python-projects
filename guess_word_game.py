import random
import os
def clear(): return os.system('clear')


words_array = ['apple', 'mango', 'blueberry']
random_word = random.choice(words_array)
print("the random word generated is: ", random_word)

game_over = False
lives = 5
livesLogo = [
    '''💣''',
    '''💣  💣''',
    '''💣  💣  💣''',
    '''💣  💣  💣  💣''',
    '''💣  💣  💣  💣  💣''',
]

guessed_word_array = []
for _ in range(len(random_word)):
    guessed_word_array += "_"

print("Guess word: ", ' '.join(guessed_word_array))

while not game_over:
    user_guess = input("Please enter a letter: ").lower()
    clear()
    for index in range(len(random_word)):
        letter = random_word[index]
        if (letter == user_guess):
            guessed_word_array[index] = letter

    if user_guess not in random_word:
        print("You loose a life")

        lives -= 1

        if lives == 0:
            game_over = True
            print("You have zero live you loose!")

    print("Guess word: ", ' '.join(guessed_word_array))

    if "_" not in guessed_word_array:
        game_over = True
        print("You won!")

    if (lives != 0):
        print("Your lives: ", livesLogo[lives-1])
