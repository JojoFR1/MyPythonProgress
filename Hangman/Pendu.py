## Programme du 22/09/2022
## Dernière modification le 26/09/2022

# Pendu
import random
import json
import time

##Settings
def settings(): #Set-up everything for the game
    global word
    global display
    global guessed
    global fail
    global err
    global limit   
    with open("Hangman/wordList.json", "r") as read_file: #TODO: Make a real list, in french
        wordList = json.load(read_file)
    
    word = random.choice(wordList)
    display = "_" * len(word)
    guessed = []
    fail = []
    err = 0
    limit = 8

def playAgain(): #Ask the user if he want to play again when he lose/win
    replay = input("\nDo you want to play again? Y/N \n")
    while replay.lower() not in ["y", "n"]:
        playAgain()
    if replay.lower() == "y":
        replay = ""
        settings()
    elif replay.lower() == "n":
        exit()
        
    
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

    if err == 8:
        print(hangman[8])
        playAgain()
        
    guess = input(hangman[err])
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2: #Check if the input is valid
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
    else: #If none of the above, the guess is wrong
        err += 1
        fail.append(guess)
        game()

    if display == word:
        print("You found the secret word, you won!")
        playAgain()

settings()
game()