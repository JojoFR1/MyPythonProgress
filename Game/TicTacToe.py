## Programme du 01/10/2022
## Dernière modification le 05/10/2022

# Tic Tac Toe
import time
scoreP1 = 0 #Set player 1 score to 0 when the program start
scoreP2 = 0 #Set player 2 score to 0 when the program start

def settings():
    global boardLayout, num, filled, player, scoreP1, scoreP2, symbol
    boardLayout = "123456789"
    num = "123456789"
    filled = []
    player = 1
    scoreP1 = scoreP1 #Keep the score between game (only when replayed)
    scoreP2 = scoreP2 #Keep the score between game (only when replayed)
    
    allowedSymbol = "OX"
    symbolSelect = input("Player 1, please select your symbol (O or X): ").upper()
    if symbolSelect not in allowedSymbol or len(symbolSelect) != 1: #Check if the input is a allowed symbol and is valid
        print("Invalid input")
        settings()
    elif symbolSelect == "O": #Check the player 1 input to set the correct order
        symbol = [symbolSelect, "X"]
        game() #BUG: When the game is replayed, it just stop the game, to fix it, this line is required
    else:
        symbol = [symbolSelect, "O"]
        game() #BUG: When the game is replayed ,it just stop the game, to fix it, this line is required

def playAgain(): #Ask the user if he want to play again when he lose/win
    replay = input("\nDo you want to play again? (Y/N) ").upper()
    if replay == "Y": #If the input = "Y", then the game restart
        settings()
    elif replay == "N": #If the input is = "N", then the program stop
        exit()
    else:
        playAgain()

def game():
    global player, boardLayout, scoreP1, scoreP2
    
    #The Tic-Tac-Toe board with multiple variants, when the game is played, when the game is finished and when the game is a tie
    board = [f'''
                             PLAYER {player} ({symbol[player-1]}) TURN
              
                                 {boardLayout[0]} | {boardLayout[1]} | {boardLayout[2]}
                                ===+===+===       SCORE
                                 {boardLayout[3]} | {boardLayout[4]} | {boardLayout[5]}     Player 1: {scoreP1}
                                ===+===+===    Player 2: {scoreP2}
                                 {boardLayout[6]} | {boardLayout[7]} | {boardLayout[8]}
                
                      Select where to place your symbol: ''', f'''
                             PLAYER {player} ({symbol[player-1]}) TURN
              
                                 {boardLayout[0]} | {boardLayout[1]} | {boardLayout[2]}
                                ===+===+===       SCORE
                                 {boardLayout[3]} | {boardLayout[4]} | {boardLayout[5]}     Player 1: {scoreP1}
                                ===+===+===    Player 2: {scoreP2}
                                 {boardLayout[6]} | {boardLayout[7]} | {boardLayout[8]}
                
                      Congrats! Player {player} ({symbol[player-1]}) won the game!''', f'''
                             PLAYER {player} ({symbol[player-1]}) TURN
              
                                 {boardLayout[0]} | {boardLayout[1]} | {boardLayout[2]}
                                ===+===+===       SCORE
                                 {boardLayout[3]} | {boardLayout[4]} | {boardLayout[5]}     Player 1: {scoreP1}
                                ===+===+===    Player 2: {scoreP2}
                                 {boardLayout[6]} | {boardLayout[7]} | {boardLayout[8]}
                
                      It's a tie! No one won, better luck next time!''']
                
    place = input(board[0])
    place.strip()
    if place == "s": #To stop the game (Dev Only!)
        exit()
    
    if place not in num or len(place) !=1: #Check if the input is a valid number and is valid
        print("Invalid input!")
        time.sleep(1)
        game()
    elif place in filled: #Check if the case is already filled
        print("This case already have a symbol!")
        time.sleep(1)
        game()
    else:
        boardLayout = boardLayout.replace(place, symbol[player-1]) #Replace the case input with the player symbol
        if player == 1: #If it was player 1 turn, then add 1 to player to become player 2.
            player += 1
        else: #If it was not player 1 turn, then remove 1 to player to become player 1.
            player -= 1
        filled.append(place)
        game()

settings()
game()