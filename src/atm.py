class InvalidPinException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InsufficientFundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ATM:
    """
    Klasa reprezentująca bankomat (ATM) z podstawowymi operacjami bankowymi.
    """
    def __init__(self, pin: int, money: float):
        self.pin = pin
        self.money = money


    def check_balance(self, pin: int) -> float:
        """
        Sprawdza saldo konta użytkownika.

        :param pin: PIN użytkownika.
        :return: Saldo konta użytkownika.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """
        if pin == self.pin:
            return self.money
        else:
            raise InvalidPinException("Nieprawidłowy pin.")

    def deposit(self, pin: int, amount: float) -> float:
        """
        Wpłaca środki na konto użytkownika.

        :param pin: PIN użytkownika.
        :param amount: Kwota do wpłacenia.
        :return: Aktualne saldo po wpłacie.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """
        if pin == self.pin:
            self.money += amount
            return self.money
        else:
            raise InvalidPinException("Nieprawidłowy pin.")

    def withdraw(self, pin: int, amount: float) -> float:
        """
        Wypłaca środki z konta użytkownika.

        :param pin: PIN użytkownika.
        :param amount: Kwota do wypłacenia.
        :return: Aktualne saldo po wypłacie.
        :raises InsufficientFundsException: Jeśli saldo jest niewystarczające.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """
        if pin == self.pin:
            if amount > self.money:
                raise InsufficientFundException("Niewystarczające środki.")
            else:
                self.money -= amount
                return self.money
        else:
            raise InvalidPinException("Nieprawidłowy pin.")

        