from extract import ExtractItem
from datetime import datetime
class Bank:

    extrato: list[ExtractItem]
    saldo: float
    today: int
    limit: int

    def __init__(self) -> None:
        self.saldo = 0
        self.extrato = []
        self.today = datetime.now().day
        self.limit = 0

    def saque(self, value: float) -> None:
        if(self.limit >= 3):
            print("Operação negada: Limite de 3 saques diario atingido")
            return
        
        if(value > self.saldo):
            print("Operação negada: Valor requerido superior ao seu saldo")
            return
        
        if(value > 500):
            print("Operação negada: Valor excede limite de R$ 500.00")
            return
    
        
        self.saldo -= abs(value)
        self.extrato.append(ExtractItem("Deposito", value, datetime.now()))

        if(self.today == datetime.now().day):
            self.limit += 1
        print(f"Saque no valor de R$ {value: .2f} realizado com sucesso")


    def deposito(self, value: float) -> None:
        if(value < 0):
            print("Operação negada. Valor tem que ser positivo")
            return
        
        self.saldo += value
        self.extrato.append(ExtractItem("Deposito", value, datetime.now()))
        print(f"Deposito no valor de R$ {value: .2f} realizado com sucesso")
        

    def mostrar_extrato(self) -> list[str]:
        for item in self.extrato:
            print(item)