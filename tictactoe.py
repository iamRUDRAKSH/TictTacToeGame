#Tic Tac Toe Game
#Two player version
def print_board(Board):
    print(f"  {Board[0]}  |  {Board[1]}  |  {Board[2]}  ")
    print("---------------")
    print(f"  {Board[3]}  |  {Board[4]}  |  {Board[5]}  ")
    print("---------------")
    print(f"  {Board[6]}  |  {Board[7]}  |  {Board[8]}  ")
def checkwin(Board):
    wins = [[0,3,6], [1,4,7], [2,5,8], [0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6]]
    for win in wins:
        if Board[win[0]] == 'X' and Board[win[1]] == 'X' and Board[win[2]] == 'X':
            return 1
        elif Board[win[0]] == 'O' and Board[win[1]] == 'O' and Board[win[2]] == 'O':
            return 2
    return -1
    
if __name__ == "__main__":
    Board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    Turn = 0
    print("Welcome to Tic Tac Toe!!")
    print("Press the number where u want to put x/o")
    print("Player 1 is X, Player 2 is O")
    print("Let's Begin.")
    print_board(Board)
    flag = 0
    while(Turn < 9):
        if(Turn % 2 == 0):
            print("Player 1's turn.")
            ans = int(input("Your response :"))
            if(Board[ans] == 'X' or Board[ans] == 'O'):
                print("Invalid move. Try again")
                continue
            Board[ans] = 'X'
        else:
            print("Player 2's turn.")
            ans = int(input("Your response :"))
            if(Board[ans] == 'X' or Board[ans] == 'O'):
                print("Invalid move. Try again")
                continue
            Board[ans] = 'O'
        Turn += 1
        print_board(Board)
        check = checkwin(Board)
        if check != -1:
            flag = 1
            break
    
    if flag == 0:
        print("It's a tie!!")
    elif flag == 1:
        if check == 1:
            print("Player 1 wins!!")
        else:
            print("Player 2 wins!!")
