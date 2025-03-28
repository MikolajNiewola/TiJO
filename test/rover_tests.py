import unittest

from src.rover import Rover


class RoverTest(unittest.TestCase):
    def setUp(self):
        x = 0
        y = 0
        self.rover = Rover(0, 0)

    def test_move_forward(self):
        # arrange
        distance = 5

        # act
        self.rover.forward(distance)
        result = self.rover.locate()

        # assert
        self.assertEqual(result, (0, 5),
                         "moving forward should return 0, 5 since starting position is 0, 0 and is facing north")

    def test_move_backwards(self):
        # arrange
        distance = 5

        # act
        self.rover.backward(distance)
        result = self.rover.locate()

        # assert
        self.assertEqual(result, (0, -5),
                         "moving forward should return 0, -5 since starting position is 0, 0 and is facing north")

    def test_move_forward_while_facing_east(self):
        # arrange
        distance = 5
        rotation = 'r'

        # act
        self.rover.rotate(rotation)
        self.rover.forward(distance)
        result = self.rover.locate()

        # assert
        self.assertEqual(result, (5, 0),
                         "moving forward should return 5, 0 since starting position is 0, 0 and is facing east")

    def test_move_forward_while_facing_west(self):
        # arrange
        distance = 5
        rotation = 'l'

        # act
        self.rover.rotate(rotation)
        self.rover.forward(distance)
        result = self.rover.locate()

        # assert
        self.assertEqual(result, (-5, 0),
                         "moving forward should return -5, 0 since starting position is 0, 0 and is facing west")

    def test_move_forward_while_facing_south(self):
        # arrange
        distance = 5
        rotation = 'l'

        # act
        self.rover.rotate(rotation)
        self.rover.rotate(rotation)
        self.rover.forward(distance)
        result = self.rover.locate()

        # assert
        self.assertEqual(result, (0, -5),
                         "moving forward should return 0, -5 since starting position is 0, 0 and is facing south")

    def test_move_forward_after_rotating_360_deg(self):
        # arrange
        distance = 5
        rotation = 'r'

        # act
        self.rover.rotate(rotation)
        self.rover.rotate(rotation)
        self.rover.rotate(rotation)
        self.rover.rotate(rotation)
        self.rover.forward(distance)
        result = self.rover.locate()

        # assert
        self.assertEqual(result, (0, 5),
                         "moving forward should return 0, 5 since starting position is 0, 0 and is facing south")


if __name__ == '__main__':
    unittest.main()
