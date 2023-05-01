import os, sys
arr = [[ " " for j in range(3)]for i in range(3)]#creating empty 3x3 matrix
coord = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
keys = [val for val in coord.keys()]

current = "X"
next = "O"

def board():
    print("=====");
    for i in range(3):
        for j in range(3):
            print(f"{arr[i][j]}",end=" ")
        print()
    print("=====");

def get_post(pos):#get the position in x and y coordinates it'll be usefull in 3x3 matrix
    pos  = int(pos)
    x,y = coord[pos]
    return arr[x][y]

def update_post(current,pos):#updates the position
    x,y = coord[pos]
    arr[x][y] = current

def get_value(player):#Get a valid input
    valid_input = False
    while not valid_input:
        pos = input(f"Player {player} enter the position: ")
        if pos.isdigit():
            pos = int(pos)
            if pos in keys:
                if get_post(pos) == " ":
                    valid_input = True
                    return pos
            
        else:
            print("Enter a valid value")

def check_empty():#checks if the box is empty
    for i in range(3):
        for j in range(3):
            if arr[i][j] == " ":
                flag = 1
                break  
            else:
                flag = 0
    return flag

def check_winner():
    winner = 0
    for i in range(3):
        # Check rows
        if arr[i][0] == arr[i][1] == arr[i][2] != " ":
            winner = arr[i][0]
            break
        # Check columns
        if arr[0][i] == arr[1][i] == arr[2][i] != " ":
            winner = arr[0][i]
            break
    # Check diagonals
    if arr[0][0] == arr[1][1] == arr[2][2] != " ":
        winner = arr[0][0]
    elif arr[0][2] == arr[1][1] == arr[2][0] != " ":
        winner = arr[0][2]

    return winner

    
def game(current,next):
    while check_empty():
        posi = get_value(current)
        update_post(current,posi)
        board()
        a = check_winner()
        if check_winner() == 0:
            game(next,current)
            
        else:
            print(f'The winner is {check_winner()}')
            sys.exit()
    
       
game(current,next)