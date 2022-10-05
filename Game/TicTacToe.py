## Programme du 01/10/2022
## Dernière modification le ../10/2022

# Tic Tac Toe
import time

def settings():
    global board, num, filled, player, symbol
    board = {'1': " ", '2': " ", '3': " ", 
            '4': " ", '5': " ", '6': " ",
            '7': " ", '8': " ", '9': " "}
    num = "123456789"
    filled = []
    player = 1
    allowedSymbol = "OX"
    symbolSelect = input("Player 1, please select your symbol, O or X: ").upper()
    if symbolSelect not in allowedSymbol or len(symbolSelect) != 1:
        print("Invalid input")
        settings()
    elif symbolSelect == "O":
        symbol = [symbolSelect, "X"]
    else:
        symbol = [symbolSelect, "O"]

def playAgain(): #Ask the user if he want to play again when he lose/win
    replay = input("\nDo you want to play again? (Y/N) ").upper()
    if replay == "Y": #If the input = "Y", then the game restart
        settings()
    elif replay == "N": #If the input is = "N", then the program stop
        exit()
    else:
        playAgain()

def game():
    global player
    layout = [f'''
                             PLAYER {player} ({symbol[player-1]}) TURN
              
                                 1 | 2 | 3
                                ===+===+===
                                 4 | 5 | 6
                                ===+===+===
                                 7 | 8 | 9
                
                      Select where to place your symbol: ''']
    # print(layout[0])
    place = input(layout[0])
    if place == "s": #To stop the game (Dev Only!)
        exit()
    place.strip()
    
    if place not in num or len(place) !=1:
        print("Invalid input!")
        time.sleep(1)
        game()
    elif place in filled:
        print("This case already have a symbol!")
        time.sleep(1)
        game()
    else:
        if player == 1:
            player += 1
        else:
            player -= 1
        board.update({place: place})
        filled.append(place)
        game()

settings()
game()