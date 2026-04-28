import random

# Board
board = [" " for _ in range(9)]

# Print board
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Check win
def check_win(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # columns
        [0,4,8],[2,4,6]           # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check draw
def check_draw():
    return " " not in board

# Player move
def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("❌ Already occupied!")
        except:
            print("⚠️ Invalid input!")

# Computer move (random)
def computer_move():
    empty = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty)
    board[move] = "O"
    print(f"💻 Computer chose position {move+1}")

# Game loop
def play_game():
    print("🎮 Tic Tac Toe - Player (X) vs Computer (O)")
    print_board()

    while True:
        player_move()
        print_board()

        if check_win("X"):
            print("🎉 You win!")
            break
        if check_draw():
            print("🤝 Draw!")
            break

        computer_move()
        print_board()

        if check_win("O"):
            print("💻 Computer wins!")
            break
        if check_draw():
            print("🤝 Draw!")
            break

# Run game
play_game()