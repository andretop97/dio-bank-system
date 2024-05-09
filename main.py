from datetime import datetime

from classes.bank import Bank
from classes.address import Address
from classes.account import Account

def account_options() -> str:
    return'''
Digite um dos valores a baixo para realizar uma operação:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => '''

def bank_options() -> str:
    return '''
Digite um dos valores a baixo para realizar uma operação:
    [1] Criar usuario
    [2] Criar conta
    [3] Listar contas para usuario
    [4] Operações da conta
    [5] Finalizar operação
    =>  '''
if __name__ == "__main__":

    bank = Bank()
    print("Bem vindo ao sistema bancario DIO Python AI Backend Developer")
    
    while True:
        command = input(bank_options())

        if command == '1':
            try:
                username = input("Informe seu nome completo: ")
                birthday = input("Informe sua data de nascimento no formato dd/mm/aaaa: ")
                birthday = datetime.strptime(birthday, "%d/%m/%Y")
                cpf = input("Informe seu cpf: ")

                print("Informações de endereço")
                city = input("Informe sua cidade: ")
                uf = input("Informe UF: ")
                neighborhood = input("Informe seu bairro: ")
                number = input("Informe o numero de endereço: ")
                square = input("Informe o logradouro: ")
                address = Address(city, uf, neighborhood, number, square)

                bank.create_user(username, birthday, cpf, address)
            except Exception as e:
                print(f"Operação negada: {e}")
        elif command == '2':
            cpf = input("Informe o CPF do usuario: ")
            bank.create_account(cpf)
        elif command == '3':
            cpf = input("Informe o CPF do usuario: ")
            accounts = bank.list_user_account(cpf)
            if not accounts:
                print("Operação negada: Não foram encontradas contas para esse usuario")
                continue
            for account in accounts:
                print(f'Account_id: {account.id} Number: {account.number} Agency: {account.agency} Saldo: {account.saldo}')
        elif command == '4':
            account_number = int(input("Insira o numero da conta : "))
            account: Account = bank.get_account(account_number)
            if not account:
                print("Operação negada: Conta não encontrada")
                continue
            while True:
                command = input(account_options())

                if command == "d":
                    valor = float(input("Informe o valor do deposito: "))
                    account.deposit(valor)
                elif command == "s":
                    valor = float(input("Informe o valor do saque: "))
                    account.withdraw(value=valor)
                elif command == "e":
                    account.show_history()
                elif command == 'q':
                    break
                else:
                    print("Comando invalido, por favor tente novamente")
        elif command == '5':
            break
        else:
            print("Comando invalido, por favor tente novamente")
        