import uuid

from datetime import datetime
from classes.address import Address

class User:
    def __init__(self, username: str, birthday: datetime, cpf: str, address: Address) -> None:
        self.username: str = username
        self.birthday: datetime = birthday
        self.cpf = cpf
        self.address = address
        self.id : uuid.UUID = uuid.uuid4()