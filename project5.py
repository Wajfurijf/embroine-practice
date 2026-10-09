import random

# Display the board
def print_board(board):
    print("\n")
    for i in range(3):
        print(" " + " | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("---+---+---")
    print()


# Check if a player has won
def check_winner(board, player):
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


# Check if board is full
def board_full(board):
    return " " not in board


# Get available moves
def available_moves(board):
    return [i for i in range(9) if board[i] == " "]


# Computer move
def computer_move(board):
    # Try to win
    for move in available_moves(board):
        board[move] = "O"
        if check_winner(board, "O"):
            return move
        board[move] = " "

    # Block player
    for move in available_moves(board):
        board[move] = "X"
        if check_winner(board, "X"):
            board[move] = " "
            return move
        board[move] = " "

    # Take center
    if board[4] == " ":
        return 4

    # Take a corner
    corners = [i for i in [0,2,6,8] if board[i] == " "]
    if corners:
        return random.choice(corners)

    # Take a side
    sides = [i for i in [1,3,5,7] if board[i] == " "]
    return random.choice(sides)


# User move
def user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in range(9) and board[move] == " ":
                return move
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")


# Main game
def play_game():
    board = [" "] * 9

    print("Welcome to Tic-Tac-Toe!")
    print("You are X, Computer is O")
    print("Board positions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    while True:
        # User turn
        print_board(board)
        move = user_move(board)
        board[move] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("🎉 Congratulations! You win!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Computer turn
        print("Computer is thinking...")
        move = computer_move(board)
        board[move] = "O"

        if check_winner(board, "O"):
            print_board(board)
            print("🤖 Computer wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()