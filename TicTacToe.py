def display_board(board):
    print('\n'*100)
    print(board[7],'|',board[8],'|',board[9])
    print('--|---|--')
    print(board[4],'|',board[5],'|',board[6])
    print('--|---|--')
    print(board[1],'|',board[2],'|',board[3])
   
def player_input():
    marker=' '
    while marker!='X' and marker!='O':
        marker=input('Player1 , Enter X or O:')
        if marker!='X' and marker!='O':
            print('Sorry, Please enter a valid input')
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X' 
    return (player1,player2)
  
def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return ((board[1]==board[2]==board[3]==mark) or (board[1]==board[4]==board[7]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) or (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark))
        
import random
def choose_first():
    if random.randint(0,1)==0:
        return 'Player 1'
    else:
        return 'Player 2'  
      
def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Enter your next position (1-9):'))
    return position

def replay():
    choice=input('Do you want to play again? (Yes or No):')
    return choice=='Yes'

print('Welcome to Tic Tac Toe!')
while True:
    gameboard=[' ']*10
    player1,player2=player_input()
    turn=choose_first()
    print(turn,' will go first.')
    play_game=input('Ready to play? Yes or No:')
    if play_game=='Yes':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='Player 1':
            display_board(gameboard)
            position=player_choice(gameboard)
            place_marker(gameboard,player1,position)
            if win_check(gameboard,player1):
                display_board(gameboard)
                print('Congratulations! ',player1,' has won the game!')
                game_on=False
            else:
                if full_board_check(gameboard):
                    display_board(gameboard)
                    print('Tie game!')
                    break
                else:
                    turn='Player 2'
        else:
            display_board(gameboard)
            position=player_choice(gameboard)
            place_marker(gameboard,player2,position)
            if win_check(gameboard,player2):
                display_board(gameboard)
                print('Congratulations! ',player2,' has won the game!')
                game_on=False
            else:
                if full_board_check(gameboard):
                    display_board(gameboard)
                    print('Tie game!')
                    break
                else:
                    turn='Player 1'
    if not replay():
        break                






