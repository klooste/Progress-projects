# tic tac toe proj 
print("Welcome to Tic Tac Toe!")

# set values for board, make variable to save values "board", use range 9 for values, use _ to make board equal to range 9 
board = [" " for _ in range(9)]
#build the board 
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")
# build check for win function, place winning combinations 
def check_win():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations: 
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False
# build check for draw function, if there are no empty spaces and the win function is not satisfied its a draw
def check_draw():
    return " " not in board 
#build player move function, create conditions for invalid responses and value errors. REMEMBER TO USE POS -1
def player_move(player): 
    while True: 
        try: 
            position = int(input(f"Player {player}, place your move(1-9): "))
            if 1 <= position <= 9 and board[position - 1] == " ": 
                return position - 1 
            else: 
                print("Please enter a valid position that has not been taken (1-9)")
        except ValueError: 
            print("Please enter a valid number (1-9)")
# build switch player function, use if/else to switch from X to O and O to X, use else to make player x if its not already. make player the perameter 
def switch_player(player): 
    return "O" if player == "X" else "X"
#set current player to X then print board 
current_player = "X"
print_board()
#execute main
while True: 
    move = player_move(current_player)
    board[move] = current_player 
    print_board()
    if check_win(): 
        print(f"Player {current_player} wins!")
        break
    elif check_draw(): 
        print("It's a draw!")
        break
    current_player = switch_player(current_player)