import unittest
from src.ShoppingCart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        print("* setUp()")
        self.shoppingCart = ShoppingCart()

    def test_add_product(self):
        print("** test_add_product()")
        # Arrange
        product_name = "Chleb"
        price = 5
        quantity = 1

        # Act
        result = self.shoppingCart.add_product(product_name, price, quantity)

        # Assert
        self.assertEqual(result, True)

    def test_remove_product(self):
        print("** test_remove_product()")
        # Arrange
        product_name = "Chleb"
        price = 5
        quantity = 1

        # Act
        self.shoppingCart.add_product(product_name, price, quantity)
        result = self.shoppingCart.remove_product(product_name)

        # Assert
        self.assertEqual(result, True)

    def test_update_quantity(self):
        print("** test_update_quantity()")
        # Arrange
        product_name = "Chleb"
        price = 5
        quantity = 1

        # Act
        self.shoppingCart.add_product(product_name, price, quantity)
        result = self.shoppingCart.update_quantity(product_name, 2)

        # Assert
        self.assertEqual(result, True)

    def tearDown(self):
        print("*** tearDown()")
        self.shoppingCart = None


if __name__ == "__main__":
    unittest.main()
