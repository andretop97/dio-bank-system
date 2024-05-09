import uuid

from datetime import datetime

from classes.extract import ExtractItem

class Account:
    def __init__(self, number: int, user_id: str, agency: str = "0001", daily_withdrawal_limit = 3, withdrawal_limit: float = 500.0) -> None:
        self.user_id = user_id
        self.number = number
        self.agency = agency
        self.id: uuid.UUID = uuid.uuid4()
        self.saldo: float = 0
        self.extract: list[ExtractItem] = []

        self.daily_withdrawal_limit = daily_withdrawal_limit
        self.withdrawal_limit = withdrawal_limit

        self.today: int = datetime.now().day
        self.daily_withdrawal_qtd = 0

    def withdraw(self, *, value) -> None:
        if self.today != datetime.now().day:
            self.today = datetime.now().day
            self.daily_withdrawal_qtd = 0

        if self.daily_withdrawal_qtd >= 3:
            print("Operação negada: Limite de 3 saques diario atingido")
            return
        
        if value > self.saldo:
            print("Operação negada: Valor requerido superior ao seu saldo")
            return
        
        if(value > 500):
            print("Operação negada: Valor excede limite de R$ 500.00")
            return
    
        
        self.saldo -= abs(value)
        self.extract.append(ExtractItem("Deposito", value, datetime.now()))

        if(self.today == datetime.now().day):
            self.daily_withdrawal_qtd += 1
        print(f"Saque no valor de R$ {value: .2f} realizado com sucesso")

    def deposit(self, /, value) -> None:
        if value < 0:
            print("Operação negada. Valor tem que ser positivo")
            return
        self.saldo += value
        self.extract.append(ExtractItem("Deposito", value, datetime.now()))
        print(f"Deposito no valor de R$ {value: .2f} realizado com sucesso")

    def show_history(self) -> None:
        for item in self.extract:
            print(item)
