import unittest

from src.math_lib import Calc


class TestCalc(unittest.TestCase):

    def setUp(self):
        print("* setUp()")
        self.calc = Calc()

    def test_add(self):
        print("** test_add()")
        # Arrange
        x = 3
        y = 2

        # Act
        result = self.calc.add(x, y)

        # Assert
        self.assertEqual(result, 5)

    def test_subtract(self):
        print("** test_subtract()")
        # Arrange
        x = 5
        y = 4

        # Act
        result = self.calc.subtract(x, y)

        # Assert
        self.assertEqual(result, 1)

    def test_divide_by_zero(self):
        print("** test_divide_by_zero()")

        # Arrange
        x = 10
        y = 0

        # Act

        # Assert
        with self.assertRaises(ValueError):
            self.calc.divide(x, y)

    def test_multiply(self):
        print("** test_multiply()")
        # Arrange
        x = 2
        y = 3

        # Act
        result = self.calc.multiply(x, y)

        # Assert
        self.assertEqual(result, 6)

    def tearDown(self):
        print("*** tearDown()")
        self.calc = None


if __name__ == "__main__":
    unittest.main()
