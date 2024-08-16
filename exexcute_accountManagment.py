# Asstrik is used to indicate "For all" ie. import everything
from bank_account import *

Goutam = BankAccount(1000, "Goutam")
Alka = BankAccount(2000, "Alka")

Goutam.get_balance()
Alka.get_balance()

Goutam.deposit(200)
Alka.deposit(500)

Goutam.withdraw(1000)
Goutam.withdraw(300)

Alka.transfer(500, Goutam)
Alka.transfer(5000, Goutam)

Tanmay = InterestRewardAcc(1000, "Tanmay")
Tanmay.get_balance()
Tanmay.deposit(100)
Tanmay.withdraw(100)
Tanmay.transfer(100, Goutam)


Vansh = SavingAccount(1000, "Vansh")
Vansh.get_balance()
Vansh.deposit(100)
Vansh.transfer(10000, Goutam)
Vansh.transfer(100, Goutam)



