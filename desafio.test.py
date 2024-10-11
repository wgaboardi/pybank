from desafio import retorna_conta_corrente


def test_retorna_conta_corrente():
    # Create a mock dictionary for CONTAS_CORRENTES
    CONTAS_CORRENTES = {1: {"cliente": 1, "agencia": "0001", "saldo": 100, "historico": []}}
    
    # Create a mock function for verificar_conta_corrente
    def verificar_conta_corrente(nr_conta):
        return nr_conta in CONTAS_CORRENTES
    
    # Call the function to be tested
    result = retorna_conta_corrente(1)
    
    # Assert that the function returns the correct account details
    assert result == {"cliente": 1, "agencia": "0001", "saldo": 100, "historico": []}