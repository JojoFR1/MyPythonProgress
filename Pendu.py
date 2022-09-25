## Programme du 22/09/2022
## Dernière modification le 24/09/2022

# Pendu
import random
# import time

##Settings
def settings():
    global word
    global display
    global guessed
    global fail
    global err
    global hangman
    
    wordList = ["Python", "Netflix", "Naruto", "Discord"]
    word = random.choice(wordList)
    display = "_" * len(word)
    guessed = []
    fail = []
    err = 0
    limit = 8
    
    hangman = [f'''
                        
                
                            Word: {display}
                            You tried: {fail}
                
                
                
                
                Input a letter to guess:''', f'''
                        
                
                            Word: {display}
                            You tried: {fail}
                
               =========
                
                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess:''', f'''
                            
                |
                |           Word: {display}
                |           You tried: {fail}
                |
               =========
                
                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess:''', f'''
                +----+       
                |    |
                |           Word: {display}
                |           You tried: {fail}
                |
               ========
                
                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess:''', f'''
                +----+      
                |/   |
                |           Word: {display}
                |           You tried: {fail}
                |
               =========
                
                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess:''', f'''
                +----+      
                |/   |
                |    O      Word: {display}
                |           You tried: {fail}
                |
               =========
                
                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess:''', f'''
                +----+      
                |/   |
                |    O      Word: {display}
                |    |      You tried: {fail}
                |
               =========
                
                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess:''', f'''
                +----+      
                |/   |
                |    O      Word: {display}
                |   /|\\    You tried: {fail}
                |
               =========
                
                Wrong guess: {limit - err} guesses remaining.
                Input a letter to guess:''', f'''
                +----+      
                |/   |
                |    O      Word: {display}
                |   /|\\    You tried: {fail}
                |   / \\
               =========
                
                Wrong guess!
                You lost, the word was {word}''']

def game():
    global word
    global display
    global guessed
    global fail
    global err
    
    print(hangman[8])
    
    guess = input()
    guess = guess.strip
    # if len(guess.strip()) == 0 or len(guess.strip()) >= 2:
    #     print("Invalid input, try again!")
    #     time.sleep(4)
    #     game()
    # 
    # elif guess in word:
    #     guessed.extend([guess])
    #     index = word.find(guess)
    #     display = display[:index] + guess + display[index + 1:]
    
    # elif guess in guessed:
    #     print("Already guessed!")
    
    # else:
    #     err += 1

settings()
game()