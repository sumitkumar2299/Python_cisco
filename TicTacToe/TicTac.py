

# Create board
board = [' ' for _ in range(9)]

# Display the board
def print_board():
    print()
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

# Check for win
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check for draw
def check_draw():
    return ' ' not in board

# Main game loop
def play_game():
    current_player = 'X'
    while True:
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != ' ' or not 0 <= move <= 8:
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        board[move] = current_player

        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
play_game()
