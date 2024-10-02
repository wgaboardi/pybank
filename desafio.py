"""
Desafio: Simular um sistema bancário com as operações de depósito, saque e extrato.
Autor: Wellington L Gaboardi (com alterações do original)
Data: 02/10/2024
Versão: 1.0
"""

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()
    if opcao == "d" or opcao=="s":
        valor = float(input(f"Informe o valor do " "depósito: " if opcao == "d" else "saque: " ))
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            continue 

    if opcao == "d":
       saldo += valor
       extrato += f"Depósito realizado no valor de: R$ {valor:10.2f}\n"

    elif opcao == "s":

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        else:
            saldo -= valor
            extrato += f"Saque realizado  no  valor  de: R$ {valor:10.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        titulo="EXTRATO BANCÁRIO"
        print(f"\n{titulo.center(35,'=')}")
        print("Conta corrente sem movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:5.2f}")
        print(f"\n{''.center(35,'=')}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
