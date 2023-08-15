from Face import Face,FaceIcon
from utils.ValidIntCheck import validInt
from RobotException import RobotException
'''
Robot:
    position
    place
    move
    left
    right
    report
    ...
'''

class Robot:

    def __init__(self)->None:
        self.x = None
        self.y = None
        self.face = None
        self.isPlaced = False

    def __str__(self):
        if self.isPlaced:
            return FaceIcon[self.face.value]
        return "The robot has not been placed"
    
    def place(self, x:int, y:int, face:Face)->None:
        # check x, y is valid
        if not validInt(x) or not validInt(y):
            raise RobotException("x or y is not a valid positive int")
        # TODO: Board size check should be check in the controller
        else:
            self.x = x
            self.y = y
            self.face = face
            self.isPlaced = True

    def move(self)->None:
        if self.face == Face.NORTH:
            self.x-=1
        elif self.face == Face.EAST:
            self.y+=1
        elif self.face == Face.NORTH:
            self.x+=1
        elif self.face == Face.WEST:
            self.y-=1

    
    def left(self):
        curFceValue = self.face.value
        newFaceValue = (curFceValue-1)%4
        curFceValue = Face[newFaceValue]


    def right(self):
        curFaceValue = self.face.value
        newFaceValue = (curFaceValue+1)%4
        self.face = Face[newFaceValue]

    def report(self):
        print(f"${self.x} ${self.y} ${self.face}")
        return (self.x, self.y,self.face )



