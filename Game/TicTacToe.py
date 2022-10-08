## Programme du 01/10/2022
## Dernière modification le 08/10/2022

# Tic Tac Toe
import time
num = "123456789" #Var to check if the input is correct
score = 0, 0 #Set player 1 and player 2 score to 0 when the program start
player = 1 #Set player to 1 only when the program start

allowedSymbol = "OX"
def symbolSelect():
    global symbol
    symbolP1 = input(f"Player 1, please select your symbol (O or X): ").upper() #Ask Player 1 to choose one of the two allowed symbol
    if symbolP1 not in allowedSymbol or len(symbolP1) != 1: #Check if the input is allowed and valid
        print("Invalid input")
        symbolSelect()
    if symbolP1 == "O": #If the input is 'O', then the Plyer 2 symbol is 'X'
        symbol = [symbolP1, "X"]
    else: #Else Player 2 symbol is 'O'
        symbol = [symbolP1, "O"]
symbolSelect()


def settings():
    global boardLayout, filled, win, move, score, solutions
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

    #WIP
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
        playAgain() #Ask the user if he wants to play again
    if move == 0: #If move is equal to zero, it means the game is a tie
        print(board[2]) #Show the tie board
        playAgain() #Ask the user if he wants to play again

    case = input(board[0]) #Ask the player where he wants to place his symbol
    case = case.strip()
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
        if player == 1: #If it was Player 1 turn, then add 1 to player to become Player 2.
            player += 1
        else: #If it was not Player 1 turn, then remove 1 to player to become Player 1.
            player -= 1
        filled.append(case) #Add the input case to the filled list
        move -= 1
        game()

settings()
game()