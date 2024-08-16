class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmmount, accName):
        self.balance = initialAmmount
        self.name = accName
        print(
            f"\nAccount '{self.name}' created.\nBalance = {self.balance:.2f}$")

    def get_balance(self):
        print(f"\n Account '{self.name}'balance = {self.balance:.2f}$")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete.")
        self.get_balance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of {self.balance:.2f}$")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.get_balance()

        except BalanceException as error:
            print(f"\nWithdraw intrrupted: {error}")

    def transfer(self, amount, account):
        try:
            print('\nBeginning Transfer..')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f'\nTransfer complete...')
        except BalanceException as error:
            print(f'\nTransfer intrrupted. {error}')


class InterestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)   # 5% reward on deposit
        print('\nDeposit Complete.')
        self.get_balance()


class SavingAccount(InterestRewardAcc):
    def __init__(self, initialAmmount, accName):
        super().__init__(initialAmmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print(f'\nwithdraw completed.')
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw intrrupted: {error}")
