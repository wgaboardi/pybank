from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Cliente:
  def __init__(self,  endereco):
    self.endereco: str = endereco
    self.contas: list = []

 
  def realizar_transacao(self, conta, transacao):
     transacao.registrar(conta)  

  def adicionar_conta(self, conta):
     self.contas.append(conta)


class PessoaFisica(Cliente):
  def __init__(self, cpf, nome, data_nascimento, endereco):
      self._cpf: str = cpf
      self._nome: str = nome
      self._data_nascimento: datetime = data_nascimento
      super().__init__(endereco)

  @property
  def cpf(self):
     return self._cpf

  @property
  def nome(self):
     return self._nome

class Conta:
  def __init__(self, numero, cliente):
     self._saldo: float = 0
     self._numero: int = numero
     self._agencia: str = "0001"
     self._cliente: Cliente = cliente
     self._historico: Historico = Historico()

  @property
  def saldo(self):
     return self._saldo
  
  @classmethod
  def nova_conta(cls, numero: int, cliente: Cliente):
     return cls(numero, cliente)

  @property
  def numero(self):
      return self._numero

  @property
  def agencia(self):
      return self._agencia

  @property
  def cliente(self):
      return self._cliente

  @property
  def historico(self):
      return self._historico  

  def sacar(self, valor: float):
    if valor > self._saldo:
       print("\nSaldo insuficiente!")
       return False
    elif valor > 0:
       self._saldo -= valor
       print("\nSaque realizado com sucesso!")
       return True
    else:
       print("\nOperação falhou!")
       return False 

  def depositar(self, valor: float):
     if valor > 0:
        self._saldo += valor
        print("\nDepósito realizado com sucesso!")
     else:
        print("\nOperação falhou!")
        return False
     return True   



class ContaCorrente(Conta):
  def __init__(self, numero, cliente, limite = 500, limite_saques = 3):   
     self._limite: float = limite
     self._limite_saques: int = limite_saques
     super().__init__(numero, cliente)
  def sacar(self, valor):
     numero_saques = len(
        [transacao for transacao in self.historico.transacoes if transacao["operacao"] == Saque.__name__]
     )

     excedeu_limite = valor > self._limite
     excedeu_saques = numero_saques >= self._limite_saques
     if excedeu_limite:
        print("\nExcedeu o valor limite de saque!")
     elif excedeu_saques:
         print("\nExcedeu número de saques!")
     else:
        return super().sacar(valor)
     return False

  def __str__(self):
        return f"""\
            Nome da Agência:\t{self.agencia}
            Conta Corrente:\t\t{self.numero}
        """

class Transacao(ABC):

  @abstractmethod       
  def registrar(self, conta: Conta):
     pass

  @property
  @abstractmethod
  def valor(self):
      pass

class Historico:
  
  def __init__(self):
    self._transacoes: list = []

  @property
  def transacoes(self):
      return self._transacoes
  def adicionar_transacao(self, transacao): # type: ignore
    reg_transacao = {"operacao" : transacao.__class__.__name__, "valor" : transacao.valor, "data" : datetime.now().strftime("%d-%m-%Y")}
    self._transacoes.append(reg_transacao)

class Deposito(Transacao):
  def __init__(self, valor:float):
    self._valor: float = valor

  @property
  def valor(self):
      return self._valor

  def registrar(self, conta):
      operacao_executada = conta.depositar(self.valor)
      if operacao_executada:
         conta.historico.adicionar_transacao(self)

class Saque(Transacao): #type: ignore
  def __init__(self, valor:float):
    self._valor: float = valor
  @property
  def valor(self):
      return self._valor

  def registrar(self, conta):
      operacao_executada = conta.sacar(self.valor)
      if operacao_executada:
         conta.historico.adicionar_transacao(self)


def menu():
    menu = """\n
    Menu Principal:
    [1] Cadastrar Cliente
    [2] Cadastrar Conta-Corrente
    [3] Depositar
    [4] Sacar
    [5] Extrato
    [6] Listar Contas-Correntes
    [0] Sair

    => """
    return  input(textwrap.dedent(menu))

def localizar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente._cpf == cpf:
            return cliente
    return None


def localizar_conta(nr_conta, contas):
    for conta in contas:
        print(conta)
        if conta.numero == nr_conta:
           return conta
    return None

def cadastrar_cliente(clientes):
    ESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

    nr_cpf_cliente = input("Informe o cpf: ")
    cliente = localizar_cliente(nr_cpf_cliente, clientes)
    if cliente:
        print("Cliente já cadastrado!")
        return
    while (1==1):
        tx_nome_cliente = input("Informe o nome: ")
        if len(tx_nome_cliente) == 0:
            continue
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
        cliente = PessoaFisica(cpf=nr_cpf_cliente, nome=tx_nome_cliente, data_nascimento=dt_nasc_cliente, endereco=endereco_cliente)
        clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")
        break

        
def cadastrar_conta_corrente(numero_conta, clientes, contas):
    # solicita o cpf do cliente
    nr_cpf = input("Informe o cpf do titular da conta: ")
    cliente = localizar_cliente(nr_cpf, clientes)
    if not cliente:
        print("Cliente não cadastrado!")
        return
    # se localizou o cliente, inclui a conta corrente
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("Conta corrente cadastrada com sucesso!")
    

def listar_contas_correntes(contas,clientes):
    print("Contas correntes cadastradas:")
    print("===============================")
    for conta in contas:
        print("Conta", conta.numero, " - ", "Cpf:", conta.cliente.cpf, "Nome:", conta.cliente.nome)


def solicitar_conta(contas):
    while (1==1):
        nr_conta = input("Informe o número da conta corrente: ")
        if nr_conta!= '':
            break
    nr_conta = int(nr_conta)
    conta_corrente = localizar_conta(nr_conta, contas)
    if not conta_corrente:
        print("Conta corrente não encontrada!")
    return conta_corrente


   
def realizar_deposito(contas):
    conta = solicitar_conta(contas)
    print(conta)
    if conta:
       cliente = conta.cliente
       valor = solicitar_valor('D')
       transacao = Deposito(valor)
       cliente.realizar_transacao(conta, transacao)

def realizar_saque(contas) -> None:
    conta = solicitar_conta(contas)
    if conta:
       cliente = conta.cliente
       valor = solicitar_valor('D')
       transacao = Saque(valor)
       cliente.realizar_transacao(conta, transacao)

def solicitar_valor(opcao: str) -> float:
    while (1==1):
        valor = input(f"Informe o valor do depósito: " if opcao.upper() == "D" else "Informe o valor do saque: ")
        if valor =='': 
            print("Operação falhou! O valor informado é inválido.")
        elif float(valor)<= 0: 
            print("Operação falhou! O valor informado não pode ser negativo.")
        else:
            break    

    return float(valor)


def emitir_extrato(conta, clientes) -> None:
    mascara_ptbr = "%d/%m/%Y %H:%M"

    titulo="EXTRATO BANCÁRIO - DATA:" + datetime.now().strftime(mascara_ptbr) 
    print(f"\n{titulo.center(35,'=')}")
    if conta: 
        print("Conta", conta.numero, " - ", "Cpf:", conta.cliente.cpf,"Nome:", conta.cliente.nome)
        print(f"Saldo atual: R$ {conta.saldo:10.2f}")
        print("=========== Lançamentos =========== ") 
        if len(conta.historico.transacoes) == 0:
            print("Conta corrente sem movimentação.")
        else:   

            for transacao in conta.historico.transacoes:
                print(f"\n{transacao['data']} - {transacao['operacao']}:\n\tR$ {transacao['valor']:.2f}")
        print(f"\n{''.center(35,'=')}")
        return

def main():
    clientes = []
    contas = []
    while True:
        opcao = menu()
        if opcao == "1":
            cadastrar_cliente(clientes)

        elif opcao == "2":
            numero_conta = len(contas) + 1  # gera um numero de conta corrente unico
            cadastrar_conta_corrente(numero_conta, clientes, contas)

        elif opcao == "3":
            realizar_deposito(contas) 

        elif opcao == "4":
            realizar_saque(contas) 

        elif opcao == "5":
            conta = solicitar_conta(contas)
            if conta:
               emitir_extrato(conta, clientes)

        elif opcao == "6":
            listar_contas_correntes(contas, clientes)

        elif opcao == "0":
            break

        else:
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")

main()