class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer


class OrderValidator:
    def __init__(self, order):
        self.order = order

    def validate_order(self):
        print("Walidacja zamowienia.")


class OrderToDatabaseator:
    def __init__(self, order):
        self.order = order

    def save_order_to_database(self):
        print("Zapisywanie zamowienia do bazy danych.")


class OrderConfirmator:
    def __init__(self, order):
        self.order = order

    def send_confirmation_email(self):
        print("Wysylanie e-maila potwierdzajacego.")


class OrderProcessor:
    def __init__(self, order):
        self.order = order
        self.validator = OrderValidator(order)
        self.databaseator = OrderToDatabaseator(order)
        self.confirmator = OrderConfirmator(order)

    def process_order(self):
        self.validator.validate_order()
        self.databaseator.save_order_to_database()
        self.confirmator.send_confirmation_email()


order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
processor = OrderProcessor(order)
processor.process_order()
