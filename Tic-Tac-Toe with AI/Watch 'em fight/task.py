# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:42:52 2020

@author: mssna
"""

import random

class TictactoeAi:
    
    def __init__(self, whitespace):
        self.cells = 9 * whitespace
        self.whoose_turn = 0
        self.isGamefinished = False
        self.x_won = "XXX"
        self.o_won = "OOO"
        self.x = None
        self.y = None
        self.second = None
        self.move_position = None
        self.move = None
        self.first = None
        self.coordinates = []
        self.turn = None
        self.first_row = None
        self.second_row = None
        self.third_row = None
        
        self.first_column = None
        self.second_column = None
        self.third_column = None
        self.diagonal1 = None
        self.diagonal2 = None


    def print_cells(self):
        print(9 * "-")
        print(f'| {self.cells[0]} {self.cells[1]} {self.cells[2]} |')
        print(f'| {self.cells[3]} {self.cells[4]} {self.cells[5]} |')
        print(f'| {self.cells[6]} {self.cells[7]} {self.cells[8]} |')
        print(9 * "-")
        
    def replacement(self):
        if self.x == 1 and self.y == 1:
            return 6
        elif self.x == 2 and self.y == 1:
            return 7
        elif self.x == 3 and self.y == 1:
            return 8
        elif self.x == 1 and self.y == 2:
            return 3
        elif self.x == 2 and self.y == 2:
            return 4
        elif self.x == 3 and self.y == 2:
            return 5
        elif self.x == 1 and self.y == 3:
            return 0
        elif self.x == 2 and self.y == 3:
            return 1
        return 2
    
    def user_move(self):
        while (True):
            self.move = input("Enter the coordinates: ")
            self.coordinates = self.move.split()
            self.first = self.coordinates[0]
            if not self.first.isdigit():
                print("You should enter numbers!")
                continue
            else:
                self.second = self.coordinates[1]
                if not self.second.isdigit():
                    print("You should enter numbers!")
                    continue
            self.x = int(self.first)
            self.y = int(self.second)
            if (self.x >= 4 or self.y >= 4 or self.x <= 0 or self.y <= 0):
                print("Coordinates should be from 1 to 3!")
                continue
            if self.cells[self.replacement()] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            break
        return self.replacement()
    
    def ai_move(self):
        return random.randrange(9)
        
    def game_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.print_cells()
        
    def build_result_map(self):
        self.first_row = str(self.cells[0] + self.cells[1] + self.cells[2])
        self.second_row = str(self.cells[3] + self.cells[4] + self.cells[5])
        self.third_row = str(self.cells[6] + self.cells[7] + self.cells[8])
    
        # column
        self.first_column = str(self.cells[0] + self.cells[3] + self.cells[6])
        self.second_column = str(self.cells[1] + self.cells[4] + self.cells[7])
        self.third_column = str(self.cells[2] + self.cells[5] + self.cells[8])
    
        # diagonal
        self.diagonal1 = str(self.cells[0] + self.cells[4] + self.cells[8])
        self.diagonal2 = str(self.cells[6] + self.cells[4] + self.cells[2])
        self.check = [self.first_row, self.second_row, self.third_row, self.first_column, self.second_column, self.third_column, self.diagonal2, self.diagonal1]
            
    def player_move(self, player):
        self.player = player
        if(self.player == "easy"):
            self.move_position = self.ai_move()
            while(self.cells[self.move_position] != " "):
                self.move_position= self.ai_move()
            print('Making move level "easy"')
            
        else:
            self.move_position = self.user_move()
            #print(type(self.move_position))
            #print((self.move_position))
        if(self.whoose_turn % 2 == 0):
            self.turn = "X"
        else: self.turn = "O"
        # 1 is replacement string len
        self.cells = self.cells[:self.move_position] + self.turn + self.cells[self.move_position + 1:]
        self.print_cells()
        self.whoose_turn += 1
        self.build_result_map()
        
    def get_result(self):
        self.build_result_map()
        if self.x_won in self.check:
            print("X wins")
            self.isGamefinished = True
        if self.o_won in self.check:
            print("O wins")
            self.isGamefinished = True 
        
    def game_start(self):
        while(not self.isGamefinished and self.whoose_turn < 9):       
            self.player_move(self.player1)
            if (self.whoose_turn > 4):
                self.get_result()
                if(self.isGamefinished):
                    break
            if(not self.isGamefinished and self.whoose_turn < 9):
                self.player_move(self.player2)
            if (self.whoose_turn > 4):
                self.get_result()
                
        
        if(not self.isGamefinished):
            print("Draw")
                           

        
while(True):
    game = TictactoeAi(" ")
    command = input("Input command: ")
    game_command = command.split()
    if(game_command[0] == "exit"):
        break
    else:
        if(len(game_command) == 3):
            game.game_players(game_command[1], game_command[2])
            game.game_start()
            
        else : 
            print("Bad parameters!")