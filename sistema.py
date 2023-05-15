#SYSTEMBANK VERSÃO 1 (Basic System)

menu = """

Digite uma Opção:
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = input("Informe o valor do depósito: ")
        valor = float(valor)

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "S":
        valor_saque = input("Digite o valor do saque: ")
        valor_saque = float(valor_saque)

        if valor_saque > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor_saque > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número de saques diário excedido.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f'Saque: R$ {valor_saque:.2f}\n'
            numero_saques += 1
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == "E":
        print("\n########## EXTRATO ##########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###############################\n")

    elif opcao == "Q":
        break

    else:
        print('Operação Inválida, por favor selecione novamente a operação desejada.')