from bank import Bank

def console() -> str:
    return'''
Digite um dos valores a baixo para realizar uma operação:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> '''

if __name__ == "__main__":

    bank = Bank()
    print("Bem vindo ao sistema bancario DIO Python AI Backend Developer")
    
    while True:
        console()
        command = input(console())

        if command == "d":
            valor = float(input("Informe o valor do deposito: "))
            bank.deposito(valor)
        elif command == "s":
            valor = float(input("Informe o valor do saque: "))
            bank.saque(valor)
        elif command == "e":
            bank.mostrar_extrato()
        elif command == 'q':
            break
        else:
            print("Comando invalido, por favor tente novamente")