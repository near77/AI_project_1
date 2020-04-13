def show_board(board_size, condition):
    if board_size == "4":
        for row in range(4):
            row_str = ""
            for col in range(4):
                row_str += "{:>3}".format(condition[row][col])
            print(row_str)
    elif board_size == "6":
        for row in range(6):
            row_str = ""
            for col in range(6):
                row_str += "{:>3}".format(condition[row][col])
            print(row_str)

    
def game():
    play_first = input("User First?(0/1)")
    game_board = input("Board Size?(4 or 6)")
    if game_board == "4":
        pass
    elif game_board == "6":
        pass
    else:
        print("Please input a legal board size.")
        game()

if __name__ == "__main__":
    condition = []
    show_board("4", condition)

