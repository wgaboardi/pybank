# Pybank - Saques, depósitos e extrato em Python
## Author: Wellington L Gaboardi
## 2024

### Melhorias implementadas:
    Aceita maiúscula/minúscula como opção
    Melhoria na visualização do extrato
    Redução do código-fonte para validar valor negativo
    Funções implementadas:
    1. cadastrar_cliente(): Este método registra um novo cliente no sistema.
    2. cadastrar_conta_corrente(): Este método registra uma nova conta bancária para um cliente.
    3. listar_contas_correntes(): Este método lista todas as contas bancárias que foram registradas no sistema.
    4. verificar_conta_corrente(nr_conta: int) -> bool: Esta função verifica se uma conta bancária específica existe no sistema.
    5. retorna_conta_corrente(nr_conta: int) -> dict: Esta função recupera os detalhes de uma conta bancária específica do dicionário CONTAS_CORRENTES.
    6. solicitar_conta() -> int: Esta função solicita que o usuário informe o número de sua conta bancária e verifica se a conta existe no sistema.
    7. atualizar_saldo(nr_conta: int, saldo: float) -> None: Esta função atualiza o saldo de uma conta bancária específica.
    8. depositar(nr_conta, saldo, valor, extrato: bool) -> None: Esta função realiza uma operação de depósito em uma conta bancária específica.
    9. sacar(nr_conta, saldo, valor, extrato: bool) -> None: Esta função realiza uma operação de retirada de uma conta bancária específica.
    10. recuperar_saldo(nr_conta: int) -> (bool, float): Esta função recupera o saldo de uma conta bancária específica.
    11. movimentacao(nr_conta: int, operacao: str, valor: float) -> None: Esta função registra uma transação financeira em uma conta bancária específica.
    12. emitir_extrato(nr_conta) -> None: Esta função gera e imprime um extrato (extrato bancário) para uma conta bancária específica.
    13. solicitar_valor(opcao: str) -> float: Esta função solicita que o usuário informe o valor do seu depósito ou retirada, dependendo do valor do parâmetro 'opcao'.
    14. atualizar_conta_corrente(nr_conta: int, saldo: float) -> None: Esta função atualiza o saldo de uma conta bancária específica. Ela recebe o número da conta bancária como entrada e o saldo atual como entrada.
    15. sacar_conta(nr_conta: int, saldo: float, valor: float) -> None: Esta função realiza uma operação de saque em uma conta bancária específica.
    16. verificar_conta_corrente(nr_conta: int, saldo: dict) -> dict: Esta função verifica se uma conta bancária específica existe no sistema.
    17. atualizar_saldo(nr_conta: int, valor: float) -> None: Esta função atualiza o saldo de uma conta bancária específica.
    18. atualizar_valor(valor: int, valor: float) -> None: Esta função recupera o valor atual do saldo de uma conta bancária específica.
    19. movimentacess(nr_conta: int, saldo) -> dict: Esta função atualiza o saldo de uma conta bancária específica.    
