## Programme du 01/10/2022
## Dernière modification le 08/10/2022

# Tic Tac Toe
import time
num = "123456789" #Var to check if the input is correct
score = 0, 0 #Set player 1 and player 2 score to 0 when the program start
player = 1 #Set player to 1 only when the program start

allowedSymbol = "O X # & $ € %"
def symbolSelect():
    global symbolP1, symbolP2
    symbolP1 = input(f"Player 1, please select your symbol ({allowedSymbol}): ").upper()
    if symbolP1 not in allowedSymbol or len(symbolP1) != 1:
        print("Invalid input")
        symbolSelect()
    symbolP2 = input(f"Player 2, please select your symbol ({allowedSymbol}): ").upper()
    if symbolP2 not in allowedSymbol or len(symbolP2) != 1: #Check if the input is a allowed symbol and is valid
        print("Invalid input")
        symbolSelect()
    if symbolP1 or symbolP2 == 's': #Stop the program (Dev only!)
        exit()
symbolSelect()


def settings():
    global boardLayout, filled, win, move, score, solutions, symbol
    boardLayout = "123456789"
    filled = []
    win = False
    move = 9
    score = score #Keep the score between game (only when replayed)
    solutions = [#Horizontal
                 [0,1,2],
                 [3,4,5],
                 [6,7,8],
                 #Vertical
                 [0,3,6],
                 [1,4,7],
                 [2,5,8],
                 #Diagonal
                 [0,4,8],
                 [2,4,6]]
    symbol = [symbolP1, symbolP2]

def playAgain(): #Ask the user if he want to play again when he lose/win
    replay = input("\nDo you want to play again? (Y/N) ").upper()
    if replay == "Y": #If the input = "Y", then the game restart
        settings()
    elif replay == "N": #If the input is = "N", then the program stop
        exit()
    else: #If the input is invalid, ask again
        playAgain()

def game():
    global boardLayout, player, score, win, move
    
    for solution in solutions:
        line = boardLayout[solution[0]] == boardLayout[solution[1]] == boardLayout[solution[2]]
        if line:
            if line == symbol[0]: #If the symbol is equal to player 1 symbol, then
                player = 1 #Set player to Player 1
                score = score[0] + 1, score[1] #Add 1 to Player 1 score, keep Player 2 score the same
                win = True
            elif line == symbol[1]: #If the symbol is equal to player 2 symbol, then
                player = 2 #Set the player to Player 2
                score = score[0], score[1] + 1 #Keep Player 1 score the same, add 1 to Player 2 score
                win = True
    
    #The Tic-Tac-Toe board with multiple variants, when the game is played, when the game is finished and when the game is a tie
    board = [f'''
                             PLAYER {player} ({symbol[player-1]}) TURN
              
                                 {boardLayout[0]} | {boardLayout[1]} | {boardLayout[2]}
                                ===+===+===       SCORE
                                 {boardLayout[3]} | {boardLayout[4]} | {boardLayout[5]}     Player 1: {score[0]}
                                ===+===+===    Player 2: {score[1]}
                                 {boardLayout[6]} | {boardLayout[7]} | {boardLayout[8]}
                
                      Select where to place your symbol: ''', f'''
                              PLAYER {player} ({symbol[player-1]}) WON
              
                                 {boardLayout[0]} | {boardLayout[1]} | {boardLayout[2]}
                                ===+===+===       SCORE
                                 {boardLayout[3]} | {boardLayout[4]} | {boardLayout[5]}     Player 1: {score[0]}
                                ===+===+===    Player 2: {score[1]}
                                 {boardLayout[6]} | {boardLayout[7]} | {boardLayout[8]}
                
                      Congrats! Player {player} ({symbol[player-1]}) won the game!''', f'''
                                 IT\'S A TIE
              
                                 {boardLayout[0]} | {boardLayout[1]} | {boardLayout[2]}
                                ===+===+===       SCORE
                                 {boardLayout[3]} | {boardLayout[4]} | {boardLayout[5]}     Player 1: {score[0]}
                                ===+===+===    Player 2: {score[1]}
                                 {boardLayout[6]} | {boardLayout[7]} | {boardLayout[8]}
                
                      It's a tie! No one won, better luck next time!''']
    if win: #If one of the player won, then ask the player if he wants to play again
        print(board[1]) #Show the winning board
        playAgain()
    if move == 0: #If move is equal to zero, it means the game is a tie
        print(board[2])
        playAgain()
    
    case = input(board[0])
    print(move)
    case.strip()
    if case == "s": #To stop the game (Dev Only!)
        exit()
    
    if case not in num or len(case) !=1: #Check if the input is a valid number and is valid
        print("Invalid input!")
        time.sleep(1)
        game()
    elif case in filled: #Check if the case is already filled
        print("This case already have a symbol!")
        time.sleep(1)
        game()
    else:
        boardLayout = boardLayout.replace(case, symbol[player-1]) #Replace the case input with the player symbol
        if player == 1: #If it was player 1 turn, then add 1 to player to become player 2.
            player += 1
        else: #If it was not player 1 turn, then remove 1 to player to become player 1.
            player -= 1
        filled.append(case) #Add the input case to the filled list
        move -= 1
        game()

settings()
game()