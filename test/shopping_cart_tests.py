import unittest
from src.ShoppingCart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        print("* setUp()")
        self.shoppingCart = ShoppingCart()
        self.emptyCart = ShoppingCart()
        self.shoppingCart.add_product("mleko", 10, 3)
        self.shoppingCart.add_product("ser", 7, 2)

    def test_add_product(self):
        print("** test_add_product()")
        # Arrange
        product_name = "chleb"
        price = 5
        quantity = 1

        # Act
        result = self.shoppingCart.add_product(product_name, price, quantity)

        # Assert
        self.assertEqual(result, True)

    def test_remove_product(self):
        print("** test_remove_product()")
        # Arrange
        product_name = "mleko"

        # Act
        result = self.shoppingCart.remove_product(product_name)

        # Assert
        self.assertEqual(result, True)

    def test_update_quantity(self):
        print("** test_update_quantity()")
        # Arrange
        product_name = "ser"
        quantity = 5

        # Act
        result = self.shoppingCart.update_quantity(product_name, quantity)

        # Assert
        self.assertEqual(result, True)

    def test_get_products(self):
        print("** test_get_products()")
        # Arrange

        # Act

        # Assert
        with self.assertRaises(ValueError):
            self.emptyCart.get_products()

    def test_count_products(self):
        print("** test_count_products()")
        # Arrange

        # Act
        result = self.shoppingCart.count_products()

        # Assert
        self.assertEqual(result, 2)

    def test_get_total_price(self):
        print("** test_get_total_price()")
        # Arrange

        # Act
        result = self.shoppingCart.get_total_price()

        # Assert
        self.assertEqual(result, 44)

    def test_apply_discount_code(self):
        print("** test_apply_discount_code()")
        # Arrange
        discount_code = "WIOSNA25"

        # Act
        result = self.shoppingCart.apply_discount_code(discount_code)

        # Assert
        self.assertEqual(result, True)

    def test_checkout(self):
        print("** test_checkout()")
        # Arrange

        # Act
        result = self.shoppingCart.checkout()

        # Assert
        self.assertEqual(result, True)

    def tearDown(self):
        print("*** tearDown()")
        self.shoppingCart = None


if __name__ == "__main__":
    unittest.main()
