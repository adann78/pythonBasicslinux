from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance #Encapsulamiento
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def _get_balance(self):
        return self.__balance
    def _set_balance(self, new_balance):
        self.__balance = new_balance
    
    @abstractmethod
    def withdraw(self, amount):
        pass #Polimorfismo
        
    
    def get_balance(self):
        return self.__balance
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        penalty=amount*0.05
        total=amount+penalty
        if total <= self._get_balance():
            self._set_balance(self._get_balance()-total)
            print(f"Withdrawal of {amount} successful with a penalty of {penalty}. New balance: {self.get_balance()}")
        else:
            print("Insufficient funds for withdrawal and penalty.")


class PlayRollAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self._get_balance():
            self._set_balance(self._get_balance()-amount)
            print(f"Withdrawal of {amount} successful. New balance: {self.get_balance()}")
        else:
            print("Insufficient funds for withdrawal.")
savings_account = SavingsAccount("Alice", 1000)
savings_account.deposit(500)
savings_account.withdraw(200)
print(f"Current balance: {savings_account.get_balance()}, Owner: {savings_account.owner}")
playroll_account = PlayRollAccount("Bob", 500)
playroll_account.deposit(300)
playroll_account.withdraw(100)
print(f"Current balance: {playroll_account.get_balance()}, Owner: {playroll_account.owner}")

