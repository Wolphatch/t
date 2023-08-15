from bin.Board import Board
from bin.Robot import Robot
from typing import Optional
from bin.Face import Face
from bin.RobotException import RobotException
from bin.utils.ValidIntCheck import validInt


class Controller:
    """
    This class acts as the interface for board and robot, combining them together.
    The class contains logic for playing the game, including interpreting user's commands.
    """
    def __init__(self, board_size: int = 5) -> None:
        """
        This method creates a game board and the robot. The default
        size for the game board is 5, however, this can be changed by the user
        :param board_size: The size of the game board, default value is 5
        """
        self.board = Board(board_size)
        self.robot = Robot()
        self.valid_commands = ["MOVE", "LEFT", "RIGHT", "REPORT"]

    def execute_command(self, command: str) -> Optional[str]:
        """
        This method interprets and runs a command entered by the user. The
        details of the commands can be found in the README.md file
        :param command: The command entered by the user
        :return: String of the robot if the command is report, none otherwise
        """
        command_list = command.split(" ")
        valid_faces = [face.name for face in Face]
        # The place command differs from the others and hence needs to be dealt differently
        if len(command_list) > 1 and command_list[0] == "PLACE":
            try:
                x_coord, y_coord, face_value = command_list[1].split(",")
                if not validInt(int(x_coord)) or not \
                        validInt(int(y_coord)) or face_value not in valid_faces:
                    raise RobotException
            except KeyError:
                raise RobotException
            except ValueError:
                raise RobotException
            else:
                if 0 <= int(x_coord) < len(self.board) and 0 <= int(y_coord) < len(self.board):
                    if not self.board.board[x_coord][y_coord]:
                        self.board.board[x_coord][ y_coord] = self.robot
                        self.robot.place(int(x_coord), int(y_coord), Face[face_value])
                    return None
                else:
                    raise RobotException(f"Position ${x_coord} ${y_coord-1} is occupied ")
        # All the other commands are single word and hence can be dealt with rather similarly
        elif command_list[0] in self.valid_commands and len(command_list) == 1:
            if command_list[0] == 'LEFT':
                if not self.robot.isPlaced():
                    raise RobotException

                self.robot.left()
                return None
            elif command_list[0] == 'RIGHT':
                if not self.robot.isPlaced():
                    raise RobotException
                self.robot.right()
                return None
            elif command_list[0] == 'MOVE':
                if not self.robot.isPlaced():
                    raise RobotException
                current_coords = (self.robot.x, self.robot.y)
                if self.robot.face == Face.WEST and 0<=current_coords[1]-1<self.board.size:
                        if self.board.board[current_coords[0]][current_coords[1] - 1] is None:
                            self.board[current_coords[0]][current_coords[1]-1] = self.robot
                            self.board[current_coords[0]][current_coords[1]] = None
                            self.robot.move()
                        else:
                            raise RobotException("New position is occupied ")
                elif self.robot.face == Face.EAST and 0<=current_coords[1]+1<self.board.size:
                        if self.board.board[current_coords[0]][current_coords[1] + 1] is None:
                            self.board[current_coords[0]][current_coords[1]+1] = self.robot
                            self.board[current_coords[0]][current_coords[1]] = None
                            self.robot.move()
                        else:
                            raise RobotException("New position is occupied ")
                elif self.robot.face == Face.NORTH and 0<=current_coords[0]-1<self.board.size:
                        if self.board.board[current_coords[0]][current_coords[0] - 1] is None:
                            self.board[current_coords[0]][current_coords[0]-1] = self.robot
                            self.board[current_coords[0]][current_coords[1]] = None
                            self.robot.move()
                        else:
                            raise RobotException("New position is occupied ")

                elif self.robot.face == Face.SOUTH and 0<=current_coords[0]+1<self.board.size:
                        if self.board.board[current_coords[0]][current_coords[0] + 1] is None:
                            self.board[current_coords[0]][current_coords[0]+1] = self.robot
                            self.board[current_coords[0]][current_coords[1]] = None
                            self.robot.move()
                        else:
                            raise RobotException("New position is occupied ")
                else:
                    raise RobotException("Move is out Of range")
            elif command_list[0] == "REPORT":
                return str(self.robot)