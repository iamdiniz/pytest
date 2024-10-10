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