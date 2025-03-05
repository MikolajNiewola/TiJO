class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        product = {product_name, price, quantity}
        self.cart.append(product)
        print(self.cart)
        return True

    def remove_product(self, product_name: str) -> bool:
        for prod in self.cart:
            if product_name in prod:
                self.cart.remove(prod)
                print(self.cart)
                return True
        else:
            return False

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        for prod in self.cart:
            if product_name in prod:
                # self.cart[prod]
                # print(self.cart)
                return True
        else:
            return False

    def get_products(self):
        """Pobieranie nazw produktów z koszyka"""
        pass

    def count_products(self) -> int:
        """Pobieranie liczby produktów znajdujących się w koszyku"""
        pass

    def get_total_price(self) -> int:
        """Pobieranie sumy cen produktów w koszyku"""
        pass

    def apply_discount_code(self, discount_code: str) -> bool:
        """Zastosowanie kuponu rabatowego"""
        pass

    def checkout(self) -> bool:
        """Realizacja zamówienia"""
        pass
