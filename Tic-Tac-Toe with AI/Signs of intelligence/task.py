import random

cells = " "
check = []
class TicTacToeAi:
    
    def __init__(self, turn, player_type):
        self.turn = turn
        self.type = player_type
        self.win_options = []
        self.defensive_options = []
           
    def print_cells(self):
        print(9 * "-")
        print(f'| {cells[0]} {cells[1]} {cells[2]} |')
        print(f'| {cells[3]} {cells[4]} {cells[5]} |')
        print(f'| {cells[6]} {cells[7]} {cells[8]} |')
        print(9 * "-")
        
    def move_on(self, move_position):
        global cells
        cells = cells[:move_position] + self.turn + cells[move_position + 1:]
        self.get_result()
        
        
    def replacement(self, x, y):
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
    
    def build_result_map(self):
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
        
        check = [first_row, second_row, third_row, first_column, 
                 second_column, third_column, diagonal2, diagonal1]
        return check
        
    def get_result(self):
        global isGameFinished, player_x, player_o
        check = self.build_result_map()
        #print(check)
        self.print_cells()
        won = str(self.turn * 3)
        if won in check:
            print(self.turn + " wins")
            isGameFinished = True
            del player_x
            del player_o
        elif cells[0:9].count(" ") == 0:
            print("Draw")
        else:
            player_o.pick_option() if self.turn == "X" else player_x.pick_option()
               
class User(TicTacToeAi):
    
    def pick_option(self):
        while(True):
            coordinates = input("Enter the coordinates: ").split()
            if not (coordinates[0].isdecimal() and coordinates[1].isdecimal()):
                print("You should enter numbers!")
                continue
            elif 3 < max(int(coordinates[0]), int(coordinates[1])):
                print("Coordinates should be from 1 to 3!")
                continue
            elif cells[self.replacement(int(coordinates[0]), int(coordinates[1]))] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                break
            
        move_position = self.replacement(int(coordinates[0]), int(coordinates[1]))
        self.move_on(move_position)

class Computer(TicTacToeAi):
    
    def ai_move(self):
        return random.randrange(9)
    
    def check_options(self, l, h, increment):
        global cells
        player = ""
        opponent = ""
        index = None
        cont = 0
        for i in range(l, h, increment):
            if cells[i] == self.turn:
                player += cells[i]
            elif cells[i] == " ":
                index = i
                cont += 1
            else:
                opponent += cells[i]
        
        if len(player) == 2 and cont == 1:
            self.win_options.append(index)
        elif len(opponent) == 2 and cont == 1:
            self.defensive_options.append(index)
            
    def pick_option(self):
        global cells
        if(self.type == "easy"):
            move_position = self.ai_move()
            while(cells[move_position] != " "):
                move_position = self.ai_move()
        elif self.type == "medium":
            self.win_options = []
            self.defensive_options = []
            
            #horizontal scan
            self.check_options(0, 3, 1)
            self.check_options(3, 6, 1)
            self.check_options(6, 9, 1)
            
            #vertical scan
            self.check_options(0, 7, 3)
            self.check_options(1, 8, 3)
            self.check_options(2, 9, 3)
            
            #diagonal scan
            self.check_options(0, 9, 4)
            self.check_options(2, 7, 2)
            
            if(len(self.win_options)> 0):
                move_position = self.win_options[0]
            elif len(self.defensive_options) > 0:
                move_position = self.defensive_options[0]
                
            else:
                move_position = self.ai_move()
                while(cells[move_position] != " "):
                    move_position = self.ai_move()    
                    
        print('Making move level "', self.type, '"', sep="")
        self.move_on(move_position)
                
def set_player_type(turn, player_type):
    if player_type == "user":
        return User(turn, player_type)
    else:
        return Computer(turn, player_type)
       
    
while True:
    isGameFinished = False
    command = input("Input command: ").split()
    if command[0] == "exit":
        break
    elif len(command) != 3 or command[0] != "start" or command[1] not in ("user", "easy", "medium") or command[2] not in ("user", "easy", "medium"):
        print("Bad parameters!")
    elif not isGameFinished:
        check = []
        cells = 9 * " "
        player_x = set_player_type("X", command[1])
        player_o = set_player_type("O", command[2])
        #print(type(player_o))
        #print(type( player_x))
        player_x.print_cells()
        player_x.pick_option()
    else:
        pass

                 