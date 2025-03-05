class ShoppingCart:
    discount_codes = ["10%", "WIOSNA25", "Mandzio"]

    def __init__(self):
        self.cart = []

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        product = {"name": product_name, "price": price, "quantity": quantity}
        self.cart.append(product)
        print(self.cart)
        return True

    def remove_product(self, product_name: str) -> bool:
        for prod in self.cart:
            if product_name == prod["name"]:
                self.cart.remove(prod)
                return True
        else:
            return False

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        for prod in self.cart:
            if product_name == prod["name"]:
                prod["quantity"] = new_quantity
                return True
        else:
            return False

    def get_products(self):
        if not self.cart:
            raise ValueError("Brak produktów")

        for prod in self.cart:
            print(prod)

    def count_products(self) -> int:
        return len(self.cart)

    def get_total_price(self) -> int:
        total_price = 0
        for prod in self.cart:
            total_price += prod["quantity"] * prod["price"]

        return total_price

    def apply_discount_code(self, discount_code: str) -> bool:
        if discount_code in self.discount_codes:
            return True

        else:
            return False

    def checkout(self) -> bool:
        if not self.cart:
            return False

        for prod in self.cart:
            self.cart.remove(prod)
        return True
