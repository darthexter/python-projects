from random import randint
# MAIN VARIABLES
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
banner = '\n### WELCOME TO TIC-TAC-TOE ###\n'
numpad = '''
Cell to Numkey mapping:

1   2   3
4   5   6
7   8   9
'''

def display_board():
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('-'*10)
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('-'*10)
    print(board[7]+' | '+board[8]+' | '+board[9]+'\n')

def welcome():
    print(banner)
    display_board()
    print(numpad)

def marker():
    '''
    OUTPUT = (player1 marker,player2 marker)
    '''
    choice = ''
    while choice not in ['X','O']:
        choice = input('Player 1: Please choose your marker "X" or "O": ').upper()
        if choice not in ['X','O']:
            print('Invalid choice! Please choose either "X" or "O"')
    if choice == 'X':
        player1 = 'X'
        player2 = 'O'
    elif choice == 'O':
        player1 = 'O'
        player2 = 'X'
    else:
        print('Marker Choice Error!')

    return (player1,player2)

def start_game():
    choice = ''
    while choice not in ['Y', 'N']:
        choice = input('Do you want to start the Game? (Y or N): ').upper()
        if choice not in ['Y', 'N']:
            print('Please enter a valid choice!')
    if choice == 'Y':
        return True
    else:
        return False

def first_move():
    p1 = p2 = None
    chance = randint(0,1)
    if chance == 0:
        return 'p1'
    else:
        return 'p2'

def marker_placement():
    choice = ''
    while choice not in range(1,10) or board[choice] != ' ':
        choice = input('Choose the cell on the Gameboard where you would like to place your marker: ')
        if choice.isdigit():
            choice = int(choice)

        if choice not in range(1,10):
            print('Please choose a valid cell (1-9)!')
        elif board[choice] != ' ':
            print('Invalid move! Cell {} is not empty'.format(pos))

    return choice

def update_gameboard(pos,marker):
    if board[pos] == ' ':
        board[pos] = marker
        return board
    else:
        pass

def board_full():
    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True

def win_check():
    # Same Row Check
    if (set(board[1:4]) == {'O'} or set(board[1:4]) == {'X'}) \
       or (set(board[4:7]) == {'O'} or set(board[4:7]) == {'X'}) \
       or (set(board[7:10]) == {'O'} or set(board[7:10]) == {'X'}):
        return True
    # Same Column Check
    elif (board[1] == board[4] == board[7] != ' ') or (board[2] == board[5] == board[8] != ' ') or (board[3] == board[6] == board[9] != ' '):
        return True
    # Same Diagonal Check
    elif (board[1] == board[5] == board[9] != ' ') or (board[3] == board[5] == board[7] != ' '):
        return True
    else:
        return False

def play_again():
    choice = input('Press "Y" to play again, any other key to quit the game.')
    if choice.upper() == 'Y':
        return True

### MAIN GAME###

# Display Welcome Screen
welcome()
# Ask Player choice
player1,player2 = marker()
# Ask if Player wants to start the Game.
gameon = start_game()
# Randomly pick player1 or player2 for first move
move = first_move()
# Gameover Checks
boardfull = board_full()
wincheck = win_check()
# Main Game Core Loop
while gameon:
    # Ask player to make a move
    if move == 'p1':
        print('Player1 Turn: \n')
        pos = marker_placement()
        update_gameboard(pos,player1)
        display_board()
        boardfull = board_full()
        wincheck = win_check()
        if wincheck:
            print('GAMEOVER - PLAYER 1 WON!! ')
            break
        elif boardfull:
            print('GAMEOVER - TIE')
            break
        else:
            move = 'p2'
    else:
        print('Player2 Turn: \n')
        pos = marker_placement()
        update_gameboard(pos,player2)
        display_board()
        boardfull = board_full()
        wincheck = win_check()
        if wincheck:
            print('GAMEOVER - PLAYER 2 WON!! ')
            break
        elif boardfull:
            print('GAMEOVER - TIE')
            break
        else:
            move = 'p1'
