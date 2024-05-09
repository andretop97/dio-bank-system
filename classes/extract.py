from datetime import datetime
class ExtractItem:
    def __init__(self, operation: str, value: float, day: datetime) -> None:
        self.operation = operation
        self.value = value
        self.day = day

    def __str__(self) -> str:
        return f'Operação: {self.operation}. Dia: {self.day.strftime("%d/%m/%Y")} Valor: R$ {self.value: .2f}'