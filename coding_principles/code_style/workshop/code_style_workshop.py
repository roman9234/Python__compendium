import math
import random


class Account:

    def __init__(self, bank, customer_name: str, customer_address: str, balance: float):
        self._account_number = Account.generate_account_number()
        self._balance = balance
        self._customer_name = customer_name
        self._customer_address = customer_address
        self._bank = bank

    def deposit(self, amount: float):
        self._bank.account_money_increase(account_number=self._account_number, amount=amount)

    def withdraw(self, amount: float):
        self._bank.account_money_decrease(account_number=self._account_number, amount=amount)

    def get_account_number(self) -> int:
        return self._account_number

    def set_account_balance(self, balance: float):
        self._balance = balance

    def get_account_balance(self) -> float:
        return self._balance
    def get_account_name(self) -> str:
        return self._customer_name

    def get_account_address(self) -> str:
        return self._customer_address

    def get_account_bank(self):
        return self._bank

    @staticmethod
    def print_name_and_balance(account):
        print(f"{account.get_account_name()}'s balance: {account.get_account_balance()}")

    @staticmethod
    def print_detailed_data(account):
        print(
            f"Account {account.get_account_number()} by {account.get_account_name()} ({account.get_account_address()}), balance {account.get_account_balance()}"
        )

    @staticmethod
    def generate_account_number() -> int:
        return math.floor(random.random() * 1000000)

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, customer_name: str, customer_address: str,
                       initial_balance: float) -> Account:
        account = Account(self, customer_name, customer_address, initial_balance)
        self.accounts[account.get_account_number()] = account
        return account

    def get_account(self, account_number: int) -> Account:
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            raise ValueError("Account not found")

    def account_money_increase(self, account_number: int, amount: float):
        self.accounts[account_number].set_account_balance(
            self.accounts[account_number].get_account_balance() + amount
        )

    def account_money_decrease(self, account_number: int, amount: float):
        if amount <= self.accounts[account_number].get_account_balance():
            self.accounts[account_number].set_account_balance(
                self.accounts[account_number].get_account_balance() - amount
            )
        else:
            raise ValueError("Insufficient funds")



class Customer:
    def __init__(self, name: str, address: str, bank: Bank):
        self.name = name
        self.address = address
        self.bank = bank

    def open_account(self, initial_balance: float) -> Account:
        account = self.bank.create_account(self.name, self.address, initial_balance)
        return account


def banking_scenario():
    bank = Bank()
    customer1 = Customer("Alice", "Moscow, Stremyannyi per, 1", bank)
    customer2 = Customer("Bob", "Vorkuta, ul. Lenina, 5", bank)

    # Alice opens an account and deposits some money
    alice_account = customer1.open_account(initial_balance=500.0)
    alice_account.deposit(100.0)
    Account.print_name_and_balance(alice_account)  # Alice's balance: 600.0

    # Bob opens an account and deposits some money
    bob_account = customer2.open_account(initial_balance=1000.0)
    bob_account.deposit(500.0)
    Account.print_name_and_balance(bob_account)  # Bob's balance: 1500.0
    # Alice withdraws some money from her account
    alice_account.withdraw(300.0)
    Account.print_name_and_balance(alice_account)  # Alice's balance: 300.0

    # Alice tries to withdraw more money than she has in her account
    try:
        alice_account.withdraw(500.0)
    except ValueError as e:
        print(e)  # Insufficient funds

    # Bank retrieves Alice's account using the account number
    retrieved_account = bank.get_account(alice_account.get_account_number())
    Account.print_detailed_data(retrieved_account) # Account XXXXXX by Alice (Moscow, Stremyannyi per, 1), _balance 300.0

banking_scenario()