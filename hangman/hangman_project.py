# Hangman Project
# 12/16/2022

import random
import csv

# Word generation

words = []
with open('hangmanWords.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        words.append(''.join(row))
        line_count += 1;
x = random.randrange(0, len(words)-1)
word = words[x]

# Other variables

lives = 9
charactersFound = 0
output = ""
for i in range(len(word)):
    output += "_"
    
gameOver = False
charExists = False

print("Welcome to Hangman, case sensitive edition. The secret word is", len(word), "letters long. If you'd like to add a word, simply enter 'add' followed by the new word.")

# Game loop

while gameOver == False:
    print('You have', lives, 'lives remaining')
    guess = str(input("Please enter a letter. If you wish to guess the word, write 'guess' followed by a space and then your word."))
    if guess[0:6] == 'guess ':
        if guess[6:] == word:
            gameOver = True
            print('GG, you guessed the word correctly!')
        else:
            print('Wrong guess.')
            print(guess[6:])
            lives -= 1
            if lives == 0:
                gameOver = True
                print('GG, you ran out of lives.')
    elif guess[0:4] == 'add ':
        with open('hangmanWords.txt', 'a') as fd:
            fd.write('\n'+guess[4:])
            fd.close()
        print('Word added.')
    elif len(guess) == 1:
        charExists = False
        for char in range(len(word)):
            if guess == word[char]:
                output = output[:char] + guess + output[char + 1:]
                charExists = True
                charactersFound += 1
        print(output)
        if charExists == False:
            lives -= 1
            if lives == 0:
                gameOver = True
                print('GG, you ran out of lives.')
        elif charactersFound == len(word):
            gameOver = True
            print('GG, you found every character!')
    else:
        print('Invalid guess. Try again.')
