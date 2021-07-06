import random
import os
import sys
from pyfiglet import Figlet
from termcolor import colored

def create_grid(dim_size):
    global hidden_grid_list
    hidden_grid_list = [['-' for row in range(dim_size)] for column in range(dim_size)]
    grid = [[0 for row in range(dim_size)] for column in range(dim_size)]
    
    print('     ', end='')
    for i in range(dim_size):
        if i < 10:
            print(i, end='     ')
        else:
            print(i, end='    ')            
    print() 

    print('------' * (dim_size+1))
    
    for i in range(dim_size):
        if i < 10:
            print(str(i) + ' |', end='')
        else:
            print(str(i) + '|', end='')
        for j in range(dim_size):
            print('  ' + hidden_grid_list[i][j] + '  |', end='')
        print()

    print('------' * (dim_size+1))

def show_hidden_grid(dim_size,num_bombs):
    global print_list
    print_list = []

    for i in range(dim_size):
        print_list.append([])
        for j in range(dim_size):
            print_list[i].append(0)

    planted_num_bomb = 0 #number of bombs planted
    while planted_num_bomb < num_bombs:
    # for i in range(num_bombs):
        random_row = random.randrange(0,dim_size-1)
        random_column = random.randrange(0, dim_size - 1)
        # check if the row_colm has a Bomb
        if print_list[random_row][random_column] == 'X': #contains the bomb
            continue #pass it
        else:
            print_list[random_row][random_column] = 'X'
            planted_num_bomb += 1

        # centre-top
        if random_row >= 1:
            if print_list[random_row - 1][random_column] != 'X':
                print_list[random_row - 1][random_column] += 1
        # right-top
        if random_row >= 1 and random_column < dim_size:
            if print_list[random_row - 1][random_column + 1] != 'X':
                print_list[random_row - 1][random_column + 1] += 1
        # right
        if random_column < dim_size:
            if print_list[random_row][random_column + 1] != 'X':
                print_list[random_row][random_column + 1] += 1
        # bottom-right
        if random_row < dim_size and random_column < dim_size:
            if print_list[random_row + 1][random_column + 1] != 'X':
                print_list[random_row + 1][random_column + 1] += 1
        # bottom
        if random_row < dim_size:
            if print_list[random_row + 1][random_column] != 'X':
                print_list[random_row + 1][random_column] += 1
        # bottom-left
        if random_row < dim_size and random_column >= 1:
            if print_list[random_row + 1][random_column - 1] != 'X':
                print_list[random_row + 1][random_column - 1] += 1
        # left
        if random_column >= 1:
            if print_list[random_row][random_column - 1] != 'X':
                print_list[random_row][random_column - 1] += 1
        # top-left
        if random_row >= 1 and random_column >= 1:
            if print_list[random_row - 1][random_column - 1] != 'X':
                print_list[random_row - 1][random_column - 1] += 1

def show_solution(dim_size,num_bombs):
    print_list = []

    for i in range(dim_size):
        print_list.append([])
        for j in range(dim_size):
            print_list[i].append(0)

    planted_num_bomb = 0 #number of bombs planted
    while planted_num_bomb < num_bombs:
    # for i in range(num_bombs):
        random_row = random.randrange(0,dim_size-1)
        random_column = random.randrange(0, dim_size - 1)
        # check if the row_colm has a Bomb
        if print_list[random_row][random_column] == 'X': #contains the bomb
            continue #pass it
        else:
            print_list[random_row][random_column] = 'X'
            planted_num_bomb += 1

        # centre-top
        if random_row >= 1:
            if print_list[random_row - 1][random_column] != 'X':
                print_list[random_row - 1][random_column] += 1
        # right-top
        if random_row >= 1 and random_column < dim_size:
            if print_list[random_row - 1][random_column + 1] != 'X':
                print_list[random_row - 1][random_column + 1] += 1
        # right
        if random_column < dim_size:
            if print_list[random_row][random_column + 1] != 'X':
                print_list[random_row][random_column + 1] += 1
        # bottom-right
        if random_row < dim_size and random_column < dim_size:
            if print_list[random_row + 1][random_column + 1] != 'X':
                print_list[random_row + 1][random_column + 1] += 1
        # bottom
        if random_row < dim_size:
            if print_list[random_row + 1][random_column] != 'X':
                print_list[random_row + 1][random_column] += 1
        # bottom-left
        if random_row < dim_size and random_column >= 1:
            if print_list[random_row + 1][random_column - 1] != 'X':
                print_list[random_row + 1][random_column - 1] += 1
        # left
        if random_column >= 1:
            if print_list[random_row][random_column - 1] != 'X':
                print_list[random_row][random_column - 1] += 1
        # top-left
        if random_row >= 1 and random_column >= 1:
            if print_list[random_row - 1][random_column - 1] != 'X':
                print_list[random_row - 1][random_column - 1] += 1

    print('     ', end='')
    for i in range(dim_size):
        if i < 10:
            print(i, end='     ')
        else:
            print(i, end='    ')            
    print() 

    print('------' * (dim_size+1))

    for row in range(dim_size):
        if row < 10:
            print(str(row) + ' |', end='')
        else:
            print(str(row) + '|', end='')
        for column in range(dim_size):
            print('  ' + str(print_list[row][column]) + '  |', end='')
        print()

    print('------' * (dim_size+1))

def update_grid(dim_size,x,y):
    hidden_grid_list[x][y] = print_list[x][y]

    print('     ', end='')
    for i in range(dim_size):
        if i < 10:
            print(i, end='     ')
        else:
            print(i, end='    ')            
    print() 

    print('------' * (dim_size+1))

    for row in range(dim_size):
        if row < 10:
            print(str(row) + ' |', end='')
        else:
            print(str(row) + '|', end='')
        for column in range(dim_size):
            print('  ' + str(hidden_grid_list[row][column]) + '  |', end='')
        print()

    print('------' * (dim_size+1))


def clear_grid():
    os.system('cls' if os.name == 'nt' else 'clear')

def createFile(playerName,Score):
    file= open("MineSweeperGame.txt","a+")
    #f=open("MineSweeperGame.txt","a+")
    file.write(playerName + ' :' + str(Score) +'\n')
    file.close()

def get_highscores():
    file_name = open('MineSweeperGame.txt','r')
    score_list = []

    for line in file_name:
        split_line = line.split()
        score_list.append(split_line)

    file_name.close

    for i in range(len(score_list)):
        print(score_list[i][0] + ' - ' + score_list[i][1])

def play():
    clear_grid()
    f = Figlet(font='slant')
    print(colored(f.renderText('MineSweeper'), 'magenta', attrs=['bold']))

    input_username = input('Enter a username: ')

    input_size = int(input('Enter the size of the grid: '))
    if input_size < 4:
        print(colored('ERROR: grid must be at least 4x4', 'red'))
        sys.exit(0)

    input_bombs = int(input('Enter the number of bombs: '))
    if input_size**2 <= input_bombs:
        print(colored('ERROR: you cannot have more bombs than squares', 'red',attrs=['bold']))
        sys.exit(0)
    if input_bombs <= 0:
        print(colored('ERROR: you cannot have 0 bombs', 'red', attrs=['bold']))
        sys.exit(0)

    input_level = input('What would you like to do? (play, show_solution, exit, show_highscores): ')

    if input_level == 'play':
        clear_grid()
        create_grid(input_size)
        show_hidden_grid(input_size,input_bombs)
        score = 0
        
        running = True
        while running:
            input_x = int(input('Type the y coordinates here: '))
            input_y = int(input('Type the x coordinates here: '))
            clear_grid()
            update_grid(input_size,input_x, input_y)
            if hidden_grid_list[input_x][input_y] == 'X':
                print(colored(f.renderText('Game Over'), 'red', attrs=['bold','blink']))
                play_again = input('Play again? (y/n): ')
                if play_again == 'y':
                    running = False
                    play()
                else:
                    running = False
            else: 
                score += 1

            print()
            print(colored('Score: ' + str(score), 'magenta', attrs=['bold','blink']))
            print()
            
            if (input_size * input_size - input_bombs == score):
                print(colored(f.renderText('You Won!'),'green', attrs=['bold']))
                running = False 

        createFile(input_username, score)     
                
    if input_level == 'show_solution':
        show_solution(input_size,input_bombs)

    if input_level == 'exit':
        sys.exit(0)

    if input_level == 'show_highscores':
        print()
        get_highscores()
        print()



play()



        





    

