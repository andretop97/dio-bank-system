from uuid import UUID
from datetime import datetime

from classes.user import User
from classes.address import Address
from classes.account import Account

from utils.list_operations import find_object_by_attribute
class Bank:
    def __init__(self) -> None:
        self.accounts: list[Account] = []
        self.users: list[User] = []
        self.count = 0

    def create_account(self, user_cpf: str) -> None:
        self.count += 1
        user: User = find_object_by_attribute(self.users, "cpf", user_cpf)
        if not user:
            print("Operação negada: CPF informado não tem usuario cadastrado")
            return
        new_account = Account(self.count, user.id)
        self.accounts.append(new_account)
        print("Conta cadastrada com sucesso")

    def create_user(self, username: str, birthday: datetime, cpf: str, address: Address) -> None:
        user = find_object_by_attribute(self.users, "cpf", cpf)
        if user:
            print("Operação negada: CPF informado ja registrado")
            return
        new_user = User(username, birthday, cpf, address)
        self.users.append(new_user)
        print("Usuario cadastrado com sucesso")

    def list_user_account(self, cpf: str) -> list[Account]:
        user: User = find_object_by_attribute(self.users, "cpf", cpf)
        if not user:
            print("Operação negada: CPF informado não tem usuario cadastrado")
            return
        return [account for account in self.accounts if account.user_id == user.id]
    
    def get_account(self, account_number: int) -> Account:
        return find_object_by_attribute(self.accounts, "number", account_number)