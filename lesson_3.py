# Инкапсуляция: protected (_name) и private (__name) атрибуты.
# private нельзя трогать снаружи напрямую — только через методы (deposit/withdraw/get_balance).


class BankAccount:
    def __init__(self, account_no):
        self._account_no = account_no   # protected — номер счёта
        self.__balance = 0              # private — баланс; меняем только через deposit/withdraw

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount to deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:    # денег не хватает -> ничего не произойдёт (ошибки нет)
            self.__balance -= amount

    # геттер — прочитать баланс снаружи (напрямую __balance недоступен)
    def get_balance(self):
        return self.__balance

igor_account = BankAccount("igor")
print(igor_account._account_no)         # protected: прочитать снаружи можно (но не принято)
igor_account._account_no = "arseniy"    # protected: и поменять можно — это лишь договорённость
# print(igor_account.__balance)         # Ошибка — private недоступен снаружи
# igor_account.__balance = 100000       # создаст НОВЫЙ атрибут, реальный баланс не изменит
# print(igor_account.__balance)
print(igor_account.get_balance())
igor_account.deposit(5000)              # нормальная сумма — баланс увеличится
# igor_account.deposit(-10000)          # бросил бы ValueError: сумма должна быть положительной
print(igor_account.get_balance())
