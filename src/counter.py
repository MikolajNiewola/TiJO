class Operation:
    def count(self, text):
        pass  # Brak implementacji

class Counter:
    def __init__(self, operation):
        self.operation = operation

    def count_characters(self, text):
        # UÅ¼ywa metody, ktÃ³ra nie jest jeszcze zaimplementowana
        return self.operation.count(text)