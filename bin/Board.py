'''
Board should include:
 - A board
functions:
 - the board should have size and return size
 - store the board in a data structure
 - put objects in the board and check it's validation
 - return current robot position

'''
import sys
from RobotException import RobotException
from utils.ValidIntCheck import validInt
from Face import Face, FaceIcon

class Board:

    '''
    Create a board
        - board
        - size
        - current board position
    '''
    def __init__(self, size):
        self.board = [[None for i in range(size)] for i in range(size)]
        self.size = size


    
    def __len__(self):
        return self.size

    def __str__(self):
        result = ""
        for i in range(len(self.size)):
            result+="| "
            for j in range(len(self.size)):
                if self.board[i][j] == None:
                    result+=" _ "
                else:
                    result+=str(self.board[i][j])
            result+=" |"
            result+="\n"








