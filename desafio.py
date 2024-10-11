"""
Desafio: Simular um sistema bancário com as operações de criar usuario, criar conta corrente, listar contas correntes, depósito, saque e extrato.
Autor: Wellington L Gaboardi (com alterações do original)
Data: 11/10/2024
Versão: 2.0
"""
from datetime import datetime 

menu = """
[1] Cadastrar Cliente
[2] Cadastrar Conta-Corrente
[3] Depositar
[4] Sacar
[5] Extrato
[6] Listar Contas-Correntes
[0] Sair

=> """

LIMITE = 500
ACUM_CONTA_CORRENTE = 0

NR_AGENCIA = "0001"
SALDO_INICIAL = 0  
CLIENTES = {} # lista dos clientes
CONTAS_CORRENTES = {} # lista das contas correntes

ESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
mascara_ptbr = "%d/%m/%Y %H:%M"

def cadastrar_cliente():
    """
    This function registers a new client in the system.

    Parameters:
    None

    Returns:
    None: This function does not return any value. It only registers the new client.

    Description:
    The function prompts the user to input the client's CPF and verifies if the client already exists in the system. If the client does not exist, the function prompts the user to input the client's personal information, such as name, date of birth, address, and state. The client's information is then stored in the CLIENTES dictionary with the CPF as the key.
    """
    global CLIENTES
    while (1==1):
        nr_cpf_cliente = input("Informe o cpf: ")
        if nr_cpf_cliente != '':
            break
    if nr_cpf_cliente in CLIENTES:
        print("Cliente já cadastrado!")
    else:
        while (1==1):
            tx_nome_cliente = input("Informe o nome: ")
            if len(tx_nome_cliente) > 0:
                break
        dt_nasc_cliente = input("Informe a data de nascimento: ")
        tx_logra_cliente = input("Informe o logradouro: ")
        nr_logra_cliente = input("Informe o número: ")
        tx_comple_cliente = input("Informe o complemento: ")
        tx_bairro_cliente = input("Informe o bairro: ")
        tx_cidade_cliente = input("Informe a cidade: ")
        while 1==1:
            tx_estado_cliente = input("Informe a sigla do Estado: ").upper()
            if tx_estado_cliente in ESTADOS:
                break
            else:
                print("Sigla de estado inválida!")
        endereco_cliente = { "logradouro" : tx_logra_cliente,
                                "numero" : nr_logra_cliente,
                                "complemento": tx_comple_cliente,
                                "bairro": tx_bairro_cliente,
                                "cidade": tx_cidade_cliente,
                                "estado": tx_estado_cliente
                                }
        cliente = {"nome" : tx_nome_cliente, "data_nascimento" : dt_nasc_cliente, "endereco" : endereco_cliente}
        CLIENTES[nr_cpf_cliente] = cliente
        print("Cliente cadastrado com sucesso!")

        
def solicitar_cliente():
    """
    This function prompts the user to input the CPF of the account holder and verifies if the client exists in the system.

    Parameters:
    None

    Returns:
    int: The CPF of the client if it exists in the system. If the client does not exist, the function returns -1.
    """
    nr_cpf = input("Informe o cpf do titular da conta: ")
    cliente_existe = nr_cpf in CLIENTES
    if cliente_existe == False:
        print("Cliente não encontrado!")
        return -1
    return nr_cpf


def cadastrar_conta_corrente():
    """
    This function registers a new bank account for a client.

    Parameters:
    None

    Returns:
    None: This function does not return any value. It only registers the new bank account.
    """
    global CONTAS_CORRENTES, ACUM_CONTA_CORRENTE
    # solicita o cpf do cliente
    id_cliente = solicitar_cliente()
    # se localizou o cliente, inclui a conta corrente
    if id_cliente != -1:
        ACUM_CONTA_CORRENTE += 1
        conta_corrente = {"cliente": id_cliente, "agencia": NR_AGENCIA, "saldo": SALDO_INICIAL, "historico": []}
        CONTAS_CORRENTES[ACUM_CONTA_CORRENTE] = conta_corrente
        print(CONTAS_CORRENTES)
    return

    

def listar_contas_correntes():
    """
    This function lists all the bank accounts that have been registered in the system.

    Parameters:
    None

    Returns:
    None: This function does not return any value. It only prints the list of registered bank accounts.
    """
    global CONTAS_CORRENTES, CLIENTES
    print("Contas correntes cadastradas:")
    print("===============================")
    for conta, result in CONTAS_CORRENTES.items():
        cliente = CLIENTES.get(result['cliente'], {})
        print("Conta", conta, " - ", "Cpf:", result['cliente'], "Nome:", cliente["nome"])


def verificar_conta_corrente(nr_conta):
    return nr_conta in CONTAS_CORRENTES

def verificar_conta_corrente(nr_conta: int) -> bool:
    """
    This function checks if a specific bank account exists in the system.

    Parameters:
    nr_conta (int): The number of the bank account to be verified.

    Returns:
    bool: True if the bank account exists in the system, False otherwise.
    """
    return nr_conta in CONTAS_CORRENTES
   

def retorna_conta_corrente(nr_conta):
    if verificar_conta_corrente(nr_conta):
       return CONTAS_CORRENTES.get(nr_conta,{})

def solicitar_conta():
    """
    This function prompts the user to input the number of their bank account and verifies if the account exists in the system.

    Parameters:
    None

    Returns:
    int: The number of the bank account if it exists in the system. If the account does not exist, the function returns -1.
    """
    global CONTAS_CORRENTES
    while (1==1):
        nr_conta = input("Informe o número da conta corrente: ")
        if nr_conta!= '':
            break
    nr_conta = int(nr_conta)
    tem_conta = verificar_conta_corrente(nr_conta)
    if tem_conta == False:
        print("Conta corrente não encontrada!")
        return -1
    return nr_conta


    
def atualizar_saldo(nr_conta: int, saldo: float) -> None:
    """
    This function updates the balance of a specific bank account.

    Parameters:
    nr_conta (int): The number of the bank account to be updated.
    saldo (float): The new balance for the specified bank account.

    Returns:
    None: This function does not return any value. It only updates the balance of the specified bank account.
    """
    global CONTAS_CORRENTES
    conta = retorna_conta_corrente(nr_conta)
    if conta != {}:
        conta["saldo"] = saldo
        CONTAS_CORRENTES[nr_conta].update(conta)

def depositar(nr_conta, saldo, valor, extrato):
    """
    This function performs a deposit operation on a specific bank account.

    Parameters:
    nr_conta (int): The number of the bank account on which the deposit will be made.
    saldo (float): The current balance of the specified bank account.
    valor (float): The amount to be deposited into the specified bank account.
    extrato (bool): A boolean value indicating whether an extrato (bank statement) should be printed after the deposit operation.

    Returns:
    None: This function does not return any value. It only performs the deposit operation and updates the balance of the specified bank account.

    If the deposit amount is greater than the allowed limit (LIMITE), the function will print an error message and return without performing the deposit operation.

    If the deposit amount would cause the balance to become negative, the function will print an error message and return without performing the deposit operation.

    After a successful deposit operation, the function will update the balance of the specified bank account, record the deposit operation in the account's history, and print the updated balance.

    If the 'extrato' parameter is set to True, the function will also print a detailed bank statement for the specified bank account, including all previous transactions.
    """
    saldo += valor
    atualizar_saldo(nr_conta, saldo)
    movimentacao(nr_conta, 'D', valor)

    if extrato == True:
        emitir_extrato(nr_conta)

    
def sacar(nr_conta, saldo, valor, extrato):
    """
    This function performs a withdrawal operation from a specific bank account.

    Parameters:
    nr_conta (int): The number of the bank account from which the withdrawal will be made.
    saldo (float): The current balance of the specified bank account.
    valor (float): The amount to be withdrawn from the specified bank account.
    extrato (bool): A boolean value indicating whether an extrato (bank statement) should be printed after the withdrawal operation.

    Returns:
    None: This function does not return any value. It only performs the withdrawal operation and updates the balance of the specified bank account.

    If the withdrawal amount is greater than the allowed limit (LIMITE), the function will print an error message and return without performing the withdrawal operation.

    If the withdrawal amount would cause the balance to become negative, the function will print an error message and return without performing the withdrawal operation.

    After a successful withdrawal operation, the function will update the balance of the specified bank account, record the withdrawal operation in the account's history, and print the updated balance.

    If the 'extrato' parameter is set to True, the function will also print a detailed bank statement for the specified bank account, including all previous transactions.
    """
    if valor > LIMITE:
        print("Operação falhou! Valor de saque superior ao permitido!", LIMITE)
        return
    if saldo - valor < 0:
        print("Operação falhou! Saldo insuficiente.")
        return
    saldo -= valor
    atualizar_saldo(nr_conta, saldo)
    movimentacao(nr_conta, 'S', valor)
    if extrato == True:
        emitir_extrato(nr_conta)


def realizar_deposito():
    """
    This function performs a deposit operation on a specific bank account.

    Parameters:
    nr_conta (int): The number of the bank account on which the deposit will be made.

    Returns:
    None: This function does not return any value. It only performs the deposit operation and updates the balance of the specified bank account.

    If the deposit amount is greater than the allowed limit (LIMITE), the function will print an error message and return without performing the deposit operation.

    If the deposit amount would cause the balance to become negative, the function will print an error message and return without performing the deposit operation.

    After a successful deposit operation, the function will update the balance of the specified bank account, record the deposit operation in the account's history, and print the updated balance.

    If the 'extrato' parameter is set to True, the function will also print a detailed bank statement for the specified bank account, including all previous transactions.
    """
    nr_conta = solicitar_conta()
    if nr_conta > -1:
        valor = solicitar_valor('D')
        conta_existe, saldo = recuperar_saldo(nr_conta)
        extrato = True
        if conta_existe == True:
            depositar(nr_conta, saldo, valor, extrato)

def realizar_saque() -> None:
    """
    This function performs a withdrawal operation from a specific bank account.

    Parameters:
    nr_conta (int): The number of the bank account from which the withdrawal will be made.
    valor (float): The amount to be withdrawn from the specified bank account.
    extrato (bool): A boolean value indicating whether an extrato (bank statement) should be printed after the withdrawal operation. Default value is "S" (True).

    Returns:
    None: This function does not return any value. It only performs the withdrawal operation and updates the balance of the specified bank account.

    If the withdrawal amount is greater than the allowed limit (LIMITE), the function will print an error message and return without performing the withdrawal operation.

    If the withdrawal amount would cause the balance to become negative, the function will print an error message and return without performing the withdrawal operation.

    After a successful withdrawal operation, the function will update the balance of the specified bank account, record the withdrawal operation in the account's history, and print the updated balance.

    If the 'extrato' parameter is set to True, the function will also print a detailed bank statement for the specified bank account, including all previous transactions.
    """
    nr_conta = solicitar_conta()
    if nr_conta > -1:
        valor = solicitar_valor('S')
        conta_existe, saldo = recuperar_saldo(nr_conta)
        extrato = True
        if conta_existe == True:
            sacar(nr_conta, saldo, valor, extrato)


def recuperar_saldo(nr_conta: int):
    """
    This function retrieves the balance of a specific bank account.

    Parameters:
    nr_conta (int): The number of the bank account for which the balance needs to be retrieved.

    Returns:
    A tuple containing a boolean value and a float. The boolean value indicates whether the specified bank account exists in the system. If the specified bank account exists, the float value represents the current balance of the account. If the specified bank account does not exist, the function returns False and 0 as the balance.
    """
    conta = CONTAS_CORRENTES.get(nr_conta, {})
    if conta == {}:
        print("Conta corrente não encontrada!")
        return False, 0
    saldo = conta['saldo']
    return True, saldo


def movimentacao(nr_conta: int, operacao: str, valor: float) -> None:
    """
    This function records a financial transaction (either a deposit or a withdrawal) on a specific bank account.

    Parameters:
    nr_conta (int): The number of the bank account on which the transaction will be made.
    operacao (str): A string representing the type of transaction. If the string is "D", the transaction is a deposit. If the string is "S", the transaction is a withdrawal.
    valor (float): The amount of the transaction.

    Returns:
    None: This function does not return any value. It only records the transaction and updates the balance of the specified bank account.

    This function first retrieves the current date and time using the `datetime.now().strftime(mascara_ptbr)` function. It then checks the value of the `operacao` parameter. If the value is "D", the function sets the `historico` variable to a string indicating that a deposit was made. If the value is "S", the function sets the `historico` variable to a string indicating that a withdrawal was made.

    The function then appends the `historico` variable to the `historico` list associated with the specified bank account in the `CONTAS_CORRENTES` dictionary. Finally, the function prints the updated `CONTAS_CORRENTES` dictionary to the console.
    """
    hoje = datetime.now().strftime(mascara_ptbr)  # Retrieves the current date and time
    if operacao.upper() == "D":  # Checks the value of the operacao parameter
        historico = f"Data {hoje} - Depósito no valor de R$ {valor:10.2f}"  # Sets the historico variable for a deposit
    else:  # If the operacao parameter is not "D", it must be "S"
        historico = f"Data {hoje} - Saque    no valor de R$ {valor:10.2f}"  # Sets the historico variable for a withdrawal
    CONTAS_CORRENTES[nr_conta]["historico"].append(historico)  # Appends the historico variable to the historico list associated with the specified bank account
    print(CONTAS_CORRENTES)  # Prints the updated CONTAS_CORRENTES dictionary to the console

def solicitar_valor(opcao: str) -> float:
    """
    This function prompts the user to input the amount of their deposit or withdrawal, depending on the value of the 'opcao' parameter.

    Parameters:
    opcao (str): A string representing the type of transaction. If the string is "D", the function prompts the user to input the deposit amount. If the string is "S", the function prompts the user to input the withdrawal amount.

    Returns:
    float: The amount of the transaction, in the form of a float.

    The function first checks if the inputted value is empty. If it is, the function prints an error message and returns None. If the inputted value is not empty, the function attempts to convert it to a float. If the conversion is successful, the function returns the float value. If the conversion fails, the function prints an error message and returns None.

    The function also checks if the inputted float value is less than or equal to zero. If it is, the function prints an error message and returns None.

    Finally, the function breaks out of the while loop and returns the float value.
    """
    while (1==1):
        valor = input(f"Informe o valor do depósito: " if opcao.upper() == "D" else "Informe o valor do saque: ")
        if valor =='': 
            print("Operação falhou! O valor informado é inválido.")
        elif float(valor)<= 0: 
            print("Operação falhou! O valor informado não pode ser negativo.")
        else:
            break    

    return float(valor)




def emitir_extrato(nr_conta) -> None:
    """
    This function generates and prints an extrato (bank statement) for a specific bank account.

    Parameters:
    nr_conta (int): The number of the bank account for which the extrato needs to be generated.

    Returns:
    None: This function does not return any value. It only generates and prints the extrato for the specified bank account.

    The function first retrieves the current date and time using the `datetime.now().strftime(mascara_ptbr)` function. It then retrieves the balance of the specified bank account using the `recuperar_saldo` function. The function then prints the title of the extrato, centered and surrounded by equal signs.

    The function then retrieves the personal information of the account holder from the `CLIENTES` dictionary using the account number as the key. It prints the account number, the account holder's CPF, and their full name.

    The function then prints the current balance of the account, formatted as a float with two decimal places.

    The function then prints a header for the transaction history, centered and surrounded by equal signs. If the specified bank account has no transaction history, the function prints a message indicating that the account has no recent transactions.

    If the specified bank account has a transaction history, the function iterates through the list of transactions and prints each one. Each transaction is printed on a new line, centered and surrounded by equal signs.

    Finally, the function prints a footer for the extrato, centered and surrounded by equal signs.
    """
    global CONTAS_CORRENTES, CLIENTES
    titulo="EXTRATO BANCÁRIO - DATA:" + datetime.now().strftime(mascara_ptbr) 
    print(f"\n{titulo.center(35,'=')}")
    id_cliente = CONTAS_CORRENTES[nr_conta]["cliente"]
    dados_cliente = CLIENTES.get(id_cliente,{})
    print("Conta", nr_conta, " - ", "Cpf:", id_cliente,"Nome:", dados_cliente["nome"])
    saldo=CONTAS_CORRENTES[nr_conta]["saldo"]
    print(f"Saldo atual: R$ {saldo:10.2f}")
    print("=========== Lançamentos =========== ") 
    if len(CONTAS_CORRENTES[nr_conta]["historico"]) == 0:
        print("Conta corrente sem movimentação.")
    else:   
        for lancamento in CONTAS_CORRENTES[nr_conta]["historico"]:
            print(lancamento)
    print(f"\n{''.center(35,'=')}")
    return


while True:

    opcao = input(menu)
    print(opcao)
    if opcao == "1":
       cadastrar_cliente()

    elif opcao == "2":
       cadastrar_conta_corrente()

    elif opcao == "3":
       realizar_deposito() 

    elif opcao == "4":
       realizar_saque() 

    elif opcao == "5":
       nr_conta = solicitar_conta()
       if nr_conta>-1:
           emitir_extrato(nr_conta)

    elif opcao == "6":
       listar_contas_correntes()

    elif opcao == "0":
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
