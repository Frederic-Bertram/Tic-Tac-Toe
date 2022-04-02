import time
import os

values = [" " for x in range(10)]
player = 1 
mark = "X"
####win flags####
win = 1
draw = -1
running = 0
stop = 1

game = running


def print_board(values):

    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[1], values[2], values[3]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[4], values[5], values[6]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[7], values[8], values[9]))
    print("\t     |     |")
    print("\n")

def check_position(x):
    if values[x] == " ":
        return True
    else:
        return False

def check_win():
    global game
    #horizontal
    if(values[1] == values[2] and values[2] == values[3] and values[1] != " "):
        game = win
    elif(values[4] == values[5] and values[5] == values[6] and values[4] != " "):
        game = win
    elif(values[7] == values[8] and values[8] == values[9] and values[7] != " "):
        game = win
    #vertical
    elif(values[1] == values[4] and values[4] == values[7] and values[1] != " "):
            game = win
    elif(values[2] == values[5] and values[5] == values[8] and values[2] != " "):
            game = win
    elif(values[3] == values[6] and values[6] == values[9] and values[3] != " "):
            game = win
    #diagonal
    elif(values[1] == values[5] and values[5] == values[9] and values[1] != " "):
            game = win
    elif(values[3] == values[5] and values[5] == values[7] and values[3] != " "):
        game = win
    #draw
    elif(values[1] != " " and values[2] != " " and values[3] != " " and values[4] != " " and values[5] != " " and values[6] != " " and values[7] != " " and values[8] != " " and values[9] != " "):
        game = draw
    else:
        game = running

print("Tic-Tac-Toe Game Designed By Frederic Bertram")    
print("Player 1 [X] --- Player 2 [O]\n")    
print()    
print()    
print("Please Wait...")    
time.sleep(3)
while (game==running):
    os.system("cls")
    print_board(values)
    if(player % 2 != 0):
        print("Player 1's turn")
        mark = "X"
    else:
        print("Player 2's turn")
        mark = "O"
    choise = int(input("Enter the position between [1-9] where you want to mark : "))
    if(check_position(choise)):
        values[choise] = mark
        player += 1
        check_win()
    else:
        print("position already taken chose another one")

os.system("cls")
print_board(values)
if(game == draw):
    print("Game Draw")
elif(game == win):
    player -= 1
    if(player % 2 != 0):
        print("Player 1 Won")
    else:
        print("player 2 won")
  







