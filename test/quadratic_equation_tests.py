import unittest
from src.quadratic_equation import QuadraticEquation


class QuadraticEquationTestCase(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):
        # arrange
        a, b, c = 0, 2, 4

        # act & assert
        self.assertRaises(ValueError, QuadraticEquation, a, b, c)

    def test_delta_less_than_zero(self):
        # arrange
        a, b, c = 1, 1, 1
        quadratic_equation = QuadraticEquation(a, b, c)

        # act
        result = quadratic_equation.solve()

        # assert
        self.assertEqual(result, None, "Should return None")

    def test_delta_equal_zero(self):
        # arrange
        a, b, c = 1, 2, 1
        quadratic_equation = QuadraticEquation(a, b, c)

        # act
        result = quadratic_equation.solve()

        # assert
        self.assertEqual(result, (-1,), "Should return -1")

    def test_delta_greater_than_zero(self):
        # arrange
        a, b, c = -5, 0, 5
        quadratic_equation = QuadraticEquation(a, b, c)

        # act
        result = quadratic_equation.solve()

        # assert
        self.assertEqual(result, (-1, 1), "Should return -1 and 1")


if __name__ == '__main__':
    unittest.main()
