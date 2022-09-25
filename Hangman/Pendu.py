## Programme du 22/09/2022
## Dernière modification le 24/09/2022

# Pendu
import random
import json
import time

# import time

##Settings
def settings():
    global word
    global display
    global guessed
    global fail
    global err
    global hangman
    
    with open("Hangman/wordList.json", "r") as read_file:
        wordList = json.load(read_file)
    
    word = random.choice(wordList)
    display = "_" * len(word)
    guessed = []
    fail = []
    err = 0
    limit = 8
    
    hangman = [f'''
                        
                
                            Word: {display}
                            You tried: {fail}
                
                
                
                
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
                |    |
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

def game():
    global word
    global display
    global guessed
    global fail
    global err

    if err == 0:
        guess = input(hangman[0])
    elif err == 1:
        guess = input(hangman[1])
    elif err == 2:
        guess = input(hangman[2])
    elif err == 3:
        guess = input(hangman[3])
    elif err == 4:
        guess = input(hangman[4])
    elif err == 5:
        guess = input(hangman[5])
    elif err == 6:
        guess = input(hangman[6])
    elif err == 7:
        guess = input(hangman[7])
    elif err == 8:
        print(hangman[8])
        exit() ##TODO: Replay system

    guess = guess.strip()
    guess = guess[0]
    ##Something is breaking here
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2: #Check if the input is valid
        print("Invalid input!")
        time.sleep(2.5)
        game()
    elif guess in guessed: #Chech if the input was already guessed
        print(f"You already guessed: {guess}!")
        time.sleep(2.5)
        game()
    elif guess in fail:
        print(f"You already tried: {guess}!")
        time.sleep(2.5)
        game()
    elif guess in word:
        guessed.extend([guess])
        index = word.find(guess)
        display = display[:index] + guess + display[index +1:]
        game()
    else:
        err += 1
        fail = fail.append([guess])
        game()

    if display == word:
        print("You found the secret word, you won!")

settings()
game()