def print_board(to_print):
    for i in range(3):
        print((to_print[i][0] + to_print[i][1] + to_print[i][2]).center(50))

def has_winner(to_search):
    return to_search[0][0] == to_search[0][1] == to_search[0][2] != "[ ]" or to_search[1][0] == to_search[1][1] == to_search[1][2] != "[ ]" or to_search[2][0] == to_search[2][1] == to_search[2][2] != "[ ]" or to_search[0][0] == to_search[1][0] == to_search[2][0] != "[ ]" or to_search[0][1] == to_search[1][1] == to_search[2][1] != "[ ]" or to_search[0][2] == to_search[1][2] == to_search[2][2] != "[ ]" or to_search[0][0] == to_search[1][1] == to_search[2][2] != "[ ]" or to_search[2][0] == to_search[1][1] == to_search[0][2] != "[ ]"


print("TIC-TAC-TOE".center(50))
board = [["[ ]", "[ ]", "[ ]"],
         ["[ ]", "[ ]", "[ ]"],
         ["[ ]", "[ ]", "[ ]"]]
for i in range(9):
    if has_winner(board):
        break
    print_board(board)
    if i % 2 == 0:
        player = 'X'
    else:
        player = 'O'
    print(f"It is Player {player}'s Turn: ".center(50))
    x = int(input("Enter the x-coordinate of your position (from 1 to 3): ".center(50)))
    y = int(input("Enter the y-coordinate of your position (from 1 to 3): ".center(50)))
    while x > 3 or x < 1 or y > 3 or y < 1 or board[3 - y][x - 1] != "[ ]":
        print("INCORRECT INPUT".center(50))
        x = int(input("Enter the x-coordinate of your position (from 1 to 3): ".center(50)))
        y = int(input("Enter the y-coordinate of your position (from 1 to 3): ".center(50)))
    board[3 - y][x - 1] = "[" + player + "]"
    i += 1
    print()
    print()
if has_winner:
    if i % 2 == 1:
        print("Congratulations Player X!".center(50))
    else:
        print("Congratulations Player O!".center(50))
else:
    print("Draw!".center(50))