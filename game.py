# Tic Tac Toe
#  first Initialize the board
# Ask for player input # Place the move on the board
 # Check for a draw or a winner # Switch player


board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw():
    return ' ' not in board

def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    print_board()

    player = 'X'
    while True:
       
        move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move, try again.")
            continue

        
        board[move] = player
        print_board()

        
        if check_winner(player):
            print(f"Player {player} wins!")
            break

       
        if check_draw():
            print("It's a draw!")
            break

        
        player = 'O' if player == 'X' else 'X'


tic_tac_toe()
