from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance


class WithdrawableAccount(BankAccount, ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass


class RegularAccount(WithdrawableAccount):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise Exception("Insufficient funds")


class SavingsAccount(WithdrawableAccount):
    def withdraw(self, amount):
        if self._balance - amount >= 100:  # Minimum balance must be 100
            self._balance -= amount
        else:
            raise Exception("Minimum balance for savings account is 100")


def perform_transaction(account: WithdrawableAccount, deposit_amount, withdraw_amount):
    account.deposit(deposit_amount)
    account.withdraw(withdraw_amount)
    print(f"Balance after transaction: {account.get_balance()}")


# Usage
regular_account = RegularAccount()
savings_account = SavingsAccount()

perform_transaction(regular_account, 500, 200)  # Works
perform_transaction(savings_account, 500, 450)  # Exception!
