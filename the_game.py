from termcolor import colored

def prRed(s): 
    print("\033[91m {}\033[00m" .format(s)) 

def prGreen(s): 
    print("\033[92m {}\033[00m" .format(s)) 

def prYellow(s): 
    print("\033[93m {}\033[00m" .format(s))

def init_board(board_size):
    board = [[0 for i in range(int(board_size))] for j in range(int(board_size))]
    return board

def init_users_hand(board_size):
    if board_size == "4":
        return([[2, 3, 5, 8, 13] for i in range(2)])
    elif board_size == "6":
        return([[2, 2, 3, 3, 5, 5, 8, 8, 8, 13, 13] for i in range(2)])

def show_hand(users_hand):
    text1 = colored("[User chess pieces]", "white", "on_green")
    text2 = colored("[  AI chess pieces]", "white", "on_yellow")
    print(text1 + ": " + str(users_hand[0]))
    print(text2 + ": " + str(users_hand[1]))

def show_board(board_size, board):
    for row in range(int(board_size)):
        row_str = ""
        for col in range(int(board_size)):
            row_str += "{:>3}".format(board[row][col])
        print(row_str)

def turns_loop(first_user, board_size, board ,users_hand):
    turn = int(first_user)
    if board_size == "4":
        while users_hand[0] != [] or users_hand[1] != []:
            if turn == 0:
                # User's turn
                step = input("Input (row, col, weight): ")
                step = step.split(" ")
                text = colored("[User]:", "white", "on_green")
                print(text + " (" + step[0] + ", " + step[1] + ", " + step[2])
                board[step[0]][step[1]] = colored(weight, "yellow")
                turn = 1
            else:
                # Computer's turn
                turn = 0
    elif board_size == "6":
        pass
       

def game():
    first_user = input("User First?(0/1) ") # 0:User 1:Computer
    board_size = input("Board Size?(4 or 6) ")
    if board_size == "4":
        users_hand = init_users_hand(board_size)
        board = init_board(board_size)
        show_board(board_size, board)
        show_hand(users_hand)
        pass
    elif board_size == "6":
        users_hand = init_users_hand(board_size)
        board = init_board(board_size)
        show_board(board_size, board)
        show_hand(users_hand)
        pass
    else:
        print("Please input a legal board size.")
        game()

if __name__ == "__main__":
    game()
