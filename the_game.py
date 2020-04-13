def init_board(board_size):
    board = [[0 for i in range(int(board_size))] for j in range(int(board_size))]
    return board

def init_users_hand(board_size):
    if board_size == "4":
        return([[2, 3, 5, 8, 13] for i in range(2)])
    elif board_size == "6":
        return([[2, 2, 3, 3, 5, 5, 8, 8, 8, 13, 13] for i in range(2)])

def show_board(board_size, board):
    for row in range(int(board_size)):
        row_str = ""
        for col in range(int(board_size)):
            row_str += "{:>3}".format(board[row][col])
        print(row_str)

def turns_loop(board_size, users_hand, board):
    pass

def game():
    first_user = input("User First?(0/1) ")
    board_size = input("Board Size?(4 or 6) ")
    if board_size == "4":
        users_hand = init_users_hand(board_size)
        board = init_board(board_size)
        show_board(board_size, board)
        pass
    elif board_size == "6":
        users_hand = init_users_hand(board_size)
        board = init_board(board_size)
        show_board(board_size, board)
        pass
    else:
        print("Please input a legal board size.")
        game()

if __name__ == "__main__":
    game()
