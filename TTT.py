# Tic Tac Toe


#variable
board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

x_move = []
o_move = []
game_move = []


# all function
def print_board():
    print( '   \t1\t\t2\t\t3\t')
    print( '   \t \t|\t \t|\t \t')
    print( ' 1 \t' + board[0][0] + '\t|\t' + board[0][1] + '\t|\t' + board[0][2] + '\t')
    print( '   \t \t|\t \t|\t \t')
    print( '    --------------------------------------------')
    print( '   \t \t|\t \t|\t \t')
    print( ' 2 \t' + board[1][0] + '\t|\t' + board[1][1] + '\t|\t' + board[1][2] + '\t')
    print( '   \t \t|\t \t|\t \t')
    print( '    --------------------------------------------')
    print( '   \t \t|\t \t|\t \t')
    print( ' 3 \t' + board[2][0] + '\t|\t' + board[2][1] + '\t|\t' + board[2][2] + '\t')
    print( '   \t \t|\t \t|\t \t')
    
def check_winner():
    if(board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'):
        return 'px'
    elif(board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'):
        return 'px'
    elif(board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):
        return 'px'
    elif(board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'):
        return 'px'
    elif(board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X'):
        return 'px'
    elif(board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
        return 'px'
    elif(board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        return 'px'
    elif(board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X'):
        return 'px'
    elif(board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):
        return 'po'
    elif(board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):
        return 'po'
    elif(board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
        return 'po'
    elif(board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'):
        return 'po'
    elif(board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'):
        return 'po'
    elif(board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
        return 'po'
    elif(board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        return 'po'
    elif(board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O'):
        return 'po'
    else:
        return 'nobody'


def px_input():
    print("Player 'X' turn")
    p1_row = input('Enter row: ')
    while(p1_row.isnumeric() != True):
        print('Invalid input please re-enter')
        p1_row = input('Enter row: ')
    while(int(p1_row)<1 or int(p1_row)>3):
        print('Invalid number please re-enter')
        p1_row = input('Enter row: ')
        while(p1_row.isnumeric() != True):
            print('Invalid input please re-enter')
            p1_row = input('Enter row: ')
    p1_col = input('Enter col: ')
    while(p1_col.isnumeric() != True):
        print('Invalid input please re-enter')
        p1_col = input('Enter col: ')
    while(int(p1_col)<1 or int(p1_col)>3):
        print('Invalid number please re-enter')
        p1_col = input('Enter col: ')
        while(p1_col.isnumeric() != True):
            print('Invalid input please re-enter')
            p1_col = input('Enter col: ')
    playermove = p1_row+p1_col
    while playermove in game_move:
        print("This position already exist please re-enter.")
        p1_row = input('Enter row: ')
        while(p1_row.isnumeric() != True):
            print('Invalid input please re-enter')
            p1_row = input('Enter row: ')
        while(int(p1_row)<1 or int(p1_row)>3):
            print('Invalid number please re-enter')
            p1_row = input('Enter row: ')
            while(p1_row.isnumeric() != True):
                print('Invalid input please re-enter')
                p1_row = input('Enter row: ')
        p1_col = input('Enter col: ')
        while(p1_col.isnumeric() != True):
            print('Invalid input please re-enter')
            p1_col = input('Enter col: ')
        while(int(p1_col)<1 or int(p1_col)>3):
            print('Invalid number please re-enter')
            p1_col = input('Enter col: ')
            while(p1_col.isnumeric() != True):
                print('Invalid input please re-enter')
                p1_col = input('Enter col: ')
        playermove = p1_row+p1_col
    x_move.append(playermove)
    game_move.append(playermove)
    row = int(p1_row)-1
    col = int(p1_col)-1
    board[row][col] = 'X'
    

def po_input():
    print("Player 'O' turn")
    p1_row = input('Enter row: ')
    while(p1_row.isnumeric() != True):
        print('Invalid input please re-enter')
        p1_row = input('Enter row: ')
    while(int(p1_row)<1 or int(p1_row)>3):
        print('Invalid number please re-enter')
        p1_row = input('Enter row: ')
        while(p1_row.isnumeric() != True):
            print('Invalid input please re-enter')
            p1_row = input('Enter row: ')
    p1_col = input('Enter col: ')
    while(p1_col.isnumeric() != True):
        print('Invalid input please re-enter')
        p1_col = input('Enter col: ')
    while(int(p1_col)<1 or int(p1_col)>3):
        print('Invalid number please re-enter')
        p1_col = input('Enter col: ')
        while(p1_col.isnumeric() != True):
            print('Invalid input please re-enter')
            p1_col = input('Enter col: ')
    playermove = p1_row+p1_col
    while playermove in game_move:
        print("This position already exist please re-enter.")
        p1_row = input('Enter row: ')
        while(p1_row.isnumeric() != True):
            print('Invalid input please re-enter')
            p1_row = input('Enter row: ')
        while(int(p1_row)<1 or int(p1_row)>3):
            print('Invalid number please re-enter')
            p1_row = input('Enter row: ')
            while(p1_row.isnumeric() != True):
                print('Invalid input please re-enter')
                p1_row = input('Enter row: ')
        p1_col = input('Enter col: ')
        while(p1_col.isnumeric() != True):
            print('Invalid input please re-enter')
            p1_col = input('Enter col: ')
        while(int(p1_col)<1 or int(p1_col)>3):
            print('Invalid number please re-enter')
            p1_col = input('Enter col: ')
            while(p1_col.isnumeric() != True):
                print('Invalid input please re-enter')
                p1_col = input('Enter col: ')
        playermove = p1_row+p1_col
    o_move.append(playermove)
    game_move.append(playermove)
    row = int(p1_row)-1
    col = int(p1_col)-1
    board[row][col] = 'O'
    

def gameplay():
    print_board()
    winner = 'nobody'
    while(winner != 'yes'):
        px_input()
        po_input()
        print_board()
        winner = check_winner()
        if(winner == 'px'):
            print("Player X win.")
            winner = 'yes'
        elif(winner == 'po'):
            print("Player O win.")
            winner = 'yes'
        elif(len(game_move)>7 and (winner != 'px' or winner != 'po')):
            print("nobody win, restart the game.")
            board[0][0] = ' '
            board[0][1] = ' '
            board[0][2] = ' '
            board[1][0] = ' '
            board[1][1] = ' '
            board[1][2] = ' '
            board[2][0] = ' '
            board[2][1] = ' '
            board[2][2] = ' '
            while game_move:
                game_move.pop()

            while x_move:
                x_move.pop()

            while o_move:
                o_move.pop()
            print_board()

    
# main method

gameplay()


    
        
        
    









