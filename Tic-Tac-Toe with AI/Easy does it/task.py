# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 00:18:45 2020

@author: mssna
"""
import random

# global Variables
whoose_turn = 0  # whoose turn X or O
cells = 9 * " "


# print game field
def print_grids():
    print(9 * "-")
    print(f'| {cells[0]} {cells[1]} {cells[2]} |')
    print(f'| {cells[3]} {cells[4]} {cells[5]} |')
    print(f'| {cells[6]} {cells[7]} {cells[8]} |')
    print(9 * "-")

# Player position
def replacement(x, y):
    if x == 1 and y == 1:
        return 6
    elif x == 2 and y == 1:
        return 7
    elif x == 3 and y == 1:
        return 8
    elif x == 1 and y == 2:
        return 3
    elif x == 2 and y == 2:
        return 4
    elif x == 3 and y == 2:
        return 5
    elif x == 1 and y == 3:
        return 0
    elif x == 2 and y == 3:
        return 1
    return 2


# handle coordinates input
def coordinates_handle():
    x = None
    y = None
    while (True):
        move = input("Enter the coordinates: ")
        coordinates = move.split()
        first = coordinates[0]
        second = None
        if not first.isdigit():
            print("You should enter numbers!")
            continue
        else:
            second = coordinates[1]
            if not second.isdigit():
                print("You should enter numbers!")
                continue
        x = int(first)
        y = int(second)
        if (x >= 4 or y >= 4 or x <= 0 or y <= 0):
            print("Coordinates should be from 1 to 3!")
            continue
        if cells[replacement(x, y)] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        break
    return replacement(x, y)

# ai move
def ai_move():
    return random.randrange(9)
# fill the cell with coordinates
def fill_the_cells():
    global cells
    move_position = None
    #move_postion = coordinates_handle()
    if whoose_turn % 2 == 0:
        move_position = coordinates_handle()
        turn = "X"
    else:
        print('Making move level "easy"')
        move_position = ai_move()
        while(cells[move_position] != " "):
            move_position = ai_move()
        turn = "O"
    # 1 is replacement string len
    cells = cells[:move_position] + turn + cells[move_position + 1:]


def win_or_draw():
    # row
    first_row = str(cells[0] + cells[1] + cells[2])
    second_row = str(cells[3] + cells[4] + cells[5])
    third_row = str(cells[6] + cells[7] + cells[8])

    # column
    first_column = str(cells[0] + cells[3] + cells[6])
    second_column = str(cells[1] + cells[4] + cells[7])
    third_column = str(cells[2] + cells[5] + cells[8])

    # diagonal
    diagonal1 = str(cells[0] + cells[4] + cells[8])
    diagonal2 = str(cells[6] + cells[4] + cells[2])
    check = [first_row, second_row, third_row, first_column, second_column, third_column, diagonal2, diagonal1]
    return check


# step 1 (print empty fields)
print_grids()

# step 2 for coordinates
got_result = False
x_won = "XXX"
o_won = "OOO"
while (whoose_turn < 9):
    # check win or draw
    if (whoose_turn > 4):
        check = win_or_draw()
        if x_won in check:
            print("X wins")
            got_result = True
            break
        if o_won in check:
            print("O wins")
            got_result = True;
            break
    fill_the_cells()
    print_grids()
    whoose_turn = whoose_turn + 1

# last turn
check = win_or_draw()
if x_won in check:
    print("X wins")
    got_result = True
if o_won in check:
    print("O wins")
    got_result = True

if (not got_result):
    print("Draw")












