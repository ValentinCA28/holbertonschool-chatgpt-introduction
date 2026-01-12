#!/usr/bin/python3
"""
Tic Tac Toe Game
Players alternate placing X/O on a 3x3 board.
First to get 3 in a row (horizontal, vertical, diagonal) wins.
"""

def print_board(board):
    """Print the current state of the Tic Tac Toe board."""
    print("\nCurrent Board:")
    print("  0 | 1 | 2 ")
    print(" -----------")
    for i, row in enumerate(board):
        print(f"{i} {' | '.join(row)} ")
        if i < 2:
            print(" -----------")
    print()

def check_winner(board):
    """
    Check if there's a winner.
    Returns 'X' if X wins, 'O' if O wins, None otherwise.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_board_full(board):
    """Check if the board is completely filled (draw condition)."""
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt):
    """Get valid integer input between 0-2, handles all errors gracefully."""
    while True:
        try:
            value = input(prompt).strip()
            num = int(value)
            if 0 <= num <= 2:
                return num
            else:
                print("Please enter 0, 1, or 2 only!")
        except ValueError:
            print("Invalid input! Please enter a number (0, 1, or 2).")
        except KeyboardInterrupt:
            print("\nGame cancelled by user.")
            exit(0)

def tic_tac_toe():
    """Main game loop for Tic Tac Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Enter row and column numbers (0, 1, or 2) to place your mark.\n")
    
    while True:
        print_board(board)
        
        # Check for winner or draw BEFORE next move
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} WINS! 🎉")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a DRAW! 🤝")
            break
        
        # Get valid move
        row = get_valid_input(f"Player {current_player} - Enter row (0, 1, 2): ")
        col = get_valid_input(f"Player {current_player} - Enter column (0, 1, 2): ")
        
        # Check if spot is taken
        if board[row][col] != " ":
            print("❌ That spot is already taken! Try again.")
            continue
        
        # Place mark
        board[row][col] = current_player
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    try:
        tic_tac_toe()
    except KeyboardInterrupt:
        print("\n\nGame cancelled.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")