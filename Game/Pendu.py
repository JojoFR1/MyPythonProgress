## Programme du 22/09/2022
## Dernière modification le 29/09/2022

# Pendu
import random
import json
import time

##Settings
def settings(): #Set-up everything for the game
    global alphabet
    global word
    global display
    global guessed
    global fail
    global err
    global limit
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open("Game/wordList.json", "r") as read_file: #TODO: Make a real list
        wordList = json.load(read_file)
    
    word = random.choice(wordList)
    word = word.upper()
    display = "_" * len(word)
    guessed = []
    fail = []
    err = 0
    limit = 8

def playAgain(): #Ask the user if he want to play again when he lose/win
    replay = input("\nDo you want to play again? (Y/N) ")
    if replay.upper() == "Y":
        replay = ""
        settings()
    elif replay.upper() == "N":
        exit()
    else:
        playAgain()

def game():
    global word
    global display
    global guessed
    global fail
    global err

    #All 9 stages of the hangman drawing
    hangman = [f'''


                            Word: {display}
                            You tried: {fail}



                You have {limit - err} guesses.
                Input a letter to guess: ''', f'''


                            Word: {display}
                            You tried: {fail}

               =========

                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess: ''', f'''

                |
                |           Word: {display}
                |           You tried: {fail}
                |
               =========

                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess: ''', f'''
                +----+
                |
                |           Word: {display}
                |           You tried: {fail}
                |
               ========

                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess: ''', f'''
                +----+
                |/   |
                |           Word: {display}
                |           You tried: {fail}
                |
               =========

                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess: ''', f'''
                +----+
                |/   |
                |    O      Word: {display}
                |           You tried: {fail}
                |
               =========

                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess: ''', f'''
                +----+
                |/   |
                |    O      Word: {display}
                |    |      You tried: {fail}
                |
               =========

                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess: ''', f'''
                +----+
                |/   |
                |    O      Word: {display}
                |   /|\\    You tried: {fail}
                |
               =========

                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess: ''', f'''
                +----+
                |/   |
                |    O      Word: {display}
                |   /|\\    You tried: {fail}
                |   / \\
               =========

                Wrong guess!
                You lost, the word was {word}!''']

    if display == word: #Check if the user won the game (found the word)
        print("You found the secret word, you won!")
        time.sleep(0.5)
        playAgain()
    if err == 8: #Check if the user lost the game (max 8 fails)
        print(hangman[8])
        time.sleep(0.5)
        playAgain()

    guess = input(hangman[err]) #Get user input to guess a letter
    if guess == "stop": #To stop the game (Dev Only!)
        exit()

    guess = guess.upper()
    guess = guess.strip()

    if guess not in alphabet or len(guess.strip()) == 0 or len(guess.strip()) >= 2: #Check if the input is a letter and is valid
        print("Invalid input!")
        time.sleep(1)
        game()
    elif guess in guessed: #Chech if the input was already guessed
        print(f"You already guessed: {guess}!")
        time.sleep(1)
        game()
    elif guess in fail: #Check if the input was already tried
        print(f"You already tried: {guess}!")
        time.sleep(1)
        game()
    elif guess in word: #Check if the input is in the word
        guessed.append(guess) #TODO: Make it so every letter that are the same appear (can stuck the game)
        index = word.find(guess)
        display = display[:index] + guess + display[index +1:]
        game()
    else: #If none of the above then the guess is wrong
        err += 1
        fail.append(guess)
        game()

settings()
game()