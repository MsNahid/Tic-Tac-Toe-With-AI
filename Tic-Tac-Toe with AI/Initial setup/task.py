# write your code here
cells = input("Enter cells: ")
cells = cells.replace("_", " ")
x_count = cells.count('X')
o_count = cells.count('O')

# print grids
def print_grids():
    print(9 * "-")
    print(f'| {cells[0]} {cells[1]} {cells[2]} |')
    print(f'| {cells[3]} {cells[4]} {cells[5]} |')
    print(f'| {cells[6]} {cells[7]} {cells[8]} |')
    print(9 * "-")
print_grids()

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

# handle coordinates input
x = None
y = None
while(True):
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
    if(x >= 4 or y >= 4 or x <= 0 or y <= 0):
        print("Coordinates should be from 1 to 3!")
        continue
    if cells[replacement(x, y)] != " ":
        print("This cell is occupied! Choose another one!")
        continue
    break

#final stage and fill the move
# fill with move
whoose_turn = ""
if(x_count == o_count): whoose_turn += "X"
else: whoose_turn += "O"
move_postion = replacement(x, y)
cells = cells[:move_postion] + whoose_turn + cells[move_postion + 1:]
print_grids()

#result
check = win_or_draw()
x_won = "XXX"
o_won = "OOO"
check = win_or_draw()
if x_won in check:
    print("X wins")
elif o_won in check:
    print("O wins")
elif " " in cells:
    print("Game not finished")
else:
    print("Draw")


