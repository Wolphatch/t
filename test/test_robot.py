from bin.Robot import Robot
from bin.Face import Face
from bin.RobotException import RobotException
import unittest

'''
test initialisation
test place
    - correct place
    - out of range

'''

class TestRobot(unittest.TestCase):
    def setUp(self) -> None:
        self.robot = Robot()

    def test_initialise(self):
        self.robot = Robot()

        self.assertEqual(self.robot.x, None)
        self.assertEqual(self.robot.y , None)
        self.assertEqual(self.robot.face, None)

    def test_robotIsPlacedCorrectly(self):
        self.robot = Robot()
        self.robot.place(1,2,Face.NORTH)

        self.assertEqual(self.robot.x, 1)
        self.assertEqual(self.robot.y, 2)
        self.assertEqual(self.robot.face,Face.NORTH)

    def test_rebotFiledToBePlacedWhenPositionIsNotPositiveInt(self):
        self.robot = Robot()
        self.assertRaises(RobotException, self.robot.place, -1, 1, Face.NORTH)

if __name__ == '__main__':
    unittest.main()