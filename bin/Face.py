'''
Robot's Face Object:
    - Allowed face direction
    - Face name
    - Face value
    - Face Icon
'''
from enum import Enum


class Face(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class FaceIcon(Enum):
    NORTH = '\u1403'
    EAST = '\u1405'
    SOUTH = '\u1401'
    WEST = '\u140A'