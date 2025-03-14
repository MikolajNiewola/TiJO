import unittest
from src.atm import ATM, InvalidPinException, InsufficientFundException


class ATMTestCase(unittest.TestCase):
    def setUp(self):
        pin = 1234
        money = 20
        self.atm = ATM(pin, money)

    def test_check_balance_wrong_pin(self):
        # arrange
        pin = 1111

        # act & assert
        self.assertRaises(InvalidPinException, self.atm.check_balance, pin)

    def test_check_balance_correct_pin(self):
        # arrange
        pin = 1234

        # act
        result = self.atm.check_balance(pin)

        # assert
        self.assertEqual(result, 20, "inputting correct pin should return amount of money on account")

    def test_deposit_wrong_pin(self):
        # arrange
        pin = 1111
        amount = 20

        # act & assert
        self.assertRaises(InvalidPinException, self.atm.deposit, pin, amount)

    def test_deposit_correct_pin(self):
        # arrange
        pin = 1234
        amount = 20

        # act
        result = self.atm.deposit(pin, amount)

        # assert
        self.assertEqual(result, 40, "Depositing 20 should return 40")

    def test_withdraw_wrong_pin(self):
        # arrange
        pin = 1111
        amount = 10

        # act & assert
        self.assertRaises(InvalidPinException, self.atm.withdraw, pin, amount)

    def test_withdraw_correct_pin_insufficient_funds(self):
        # arrange
        pin = 1234
        amount = 30

        # act & assert
        self.assertRaises(InsufficientFundException, self.atm.withdraw, pin, amount)

    def test_withdraw_correct_pin_sufficient_funds(self):
        # arrange
        pin = 1234
        amount = 20

        # act
        result = self.atm.withdraw(pin, amount)

        # assert
        self.assertEqual(result, 0, "Withdrawing 20 should return 0")

if __name__ == '__main__':
    unittest.main()
