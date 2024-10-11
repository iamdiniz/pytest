from pytest import mark

def verificar_se_e_impar_ou_par(entrada):
    if entrada % 2 == 0:
        print("Par")
        return True
    else:
        print("Impar")
        return False

def verificar_idade(idade):
    if idade == 18:
        return 1 
    return 0

@mark.verificarIdade
def test_quando_idade_for_18_entao_deve_retornar_1():
    entrada = 17
    esperado = 1
    
    resultado = verificar_idade(entrada)
    
    assert resultado == esperado
    
@mark.verificarNome
def test_quando_nome_for_sucesso_entao_deve_retornar_1():
    entrada = "sucesso"
    esperado = "sucesso"
    
    resultado = entrada
    
    assert resultado == esperado
    
@mark.skip(reason="Não terminei")
def test_quando_idade_for_18_entao_deve_retornar_1():
    entrada = 10
    esperado = 1
    
    resultado = verificar_idade(entrada)
    
    assert resultado == esperado
    
@mark.parametrizado    
@mark.parametrize( 
    'entrada, esperado',
    [(2, True), (1, False), (4, True), (3, False)]
) # Quando tiver entrada e esperado, colocasse o par chave e valor como se fosse: entrada & esperado
def test_deve_retornar_valor_esperado(entrada, esperado):
    resultado = verificar_se_e_impar_ou_par(entrada)
    
    assert resultado == esperado
    
def somar_algo(numero1, numero2):
    print("Entrei aqui")
    soma = numero1 + numero2
    return soma
    
# Pra testar isso eu preciso estar no contexto do stout
@mark.stdout
def test_somar_algo_deve_retornar_entrei_aqui_na_tela(capsys): # Fixture, para testar eu preciso estar no contexto.
    somar_algo(5, 5) # Por isso o capsys entra no contexto do console.
    saida_do_console = capsys.readouterr() # Leia as saidas
    assert saida_do_console.out == "Entrei aqui ou não?"