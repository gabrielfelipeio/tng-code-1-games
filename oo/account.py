

class Account:

    def __init__(self, number, holder, balance, limit):
        print("Build object...")
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def extract(self):
        print("{} has {} of balance".format(self.__holder, self.__balance))

    def deposit(self, value):
        self.__balance += value

    def __can_withdraw(self, amount_to_withdraw):
        amount_available_to_withdraw = self.__balance + self.__limit
        return amount_to_withdraw <= amount_available_to_withdraw

    def withdraw(self, value):
        if(self.__can_withdraw(value)):
            self.__balance -= value
        else:
            print("The amount {} exceeded the withdrawal limit".format(value))

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def banks_codes():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}