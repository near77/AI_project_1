def init_board(board_size):
    board = [[0 for i in range(int(board_size))] for j in range(int(board_size))]
    return board

def init_users_hand(board_size):
    

def show_board(board_size, board):
    for row in range(int(board_size)):
        row_str = ""
        for col in range(int(board_size)):
            row_str += "{:>3}".format(board[row][col])
        print(row_str)

def game():
    first_user = input("User First?(0/1)")
    board_size = input("Board Size?(4 or 6)")
    if board_size == "4":
        board = init_board(board_size)
        show_board()
        pass
    elif board_size == "6":
        board = init_board(board_size)
        show_board()
        pass
    else:
        print("Please input a legal board size.")
        game()

if __name__ == "__main__":
    game()
