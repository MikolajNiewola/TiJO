class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer


class OrderValidator:
    def validate_order(self, order):
        print("Walidacja zamowienia.")


class OrderToDatabaseator:

    def save_order_to_database(self, order):
        print("Zapisywanie zamowienia do bazy danych.")


class OrderConfirmator:

    def send_confirmation_email(self, order):
        print("Wysylanie e-maila potwierdzajacego.")


class OrderProcessor:
    def __init__(self, order, validator, databaseator, confirmator):
        self.order = order
        self.validator = validator
        self.databaseator = databaseator
        self.confirmator = confirmator

    def process_order(self):
        self.validator.validate_order(self.order)
        self.databaseator.save_order_to_database(self.order)
        self.confirmator.send_confirmation_email(self.order)


order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
processor = OrderProcessor(order, OrderValidator(), OrderToDatabaseator(), OrderConfirmator())
processor.process_order()
