# Задача 3
# Инструкция: Создайте класс Банковский Счет (Account).
# Определите  атрибут баланс в инициализаторе init, который инициализируется с нулевым значением.
# Создайте метод пополнение, который принимает сумму и увеличивает баланс на эту сумму.
# Создайте метод снятие, который принимает сумму и уменьшает баланс на эту сумму, если на счету достаточно средств.
# В противном случае, выводит сообщение о недостаточном балансе.
# Создайте метод показать баланс, который печатает текущий баланс счета.


class Account:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счёт. Ваш баланс теперь - {self.balance} руб.")

    def withdraw(self, money):
        if money > self.balance:
            print("Недостаточно средств.")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} руб. Ваш баланс теперь - {self.balance} руб.")

    def all_balance(self):
        print(f"Ваш баланс - {self.balance} руб.")

man = Account("id: 12345, money: 1000")

man.all_balance()
man.deposit(500)
man.withdraw(500)
man.withdraw(10000)
man.deposit(20000)
man.all_balance()





