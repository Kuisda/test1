from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance_list = balance
        self.n = len(balance)
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1>self.n or account2 >self.n:
            return False
        if self.balance_list[account1-1]>=money:
            self.balance_list[account1-1]-=money
            self.balance_list[account2-1]+=money
            return True
        return False    

    def deposit(self, account: int, money: int) -> bool:
        if account >self.n:
            return False
        self.balance_list[account-1]+=money
        return True    

    def withdraw(self, account: int, money: int) -> bool:
        if account >self.n:
            return False
        if self.balance_list[account-1] <money:
            return False    
        self.balance_list[account-1]-=money
        return True