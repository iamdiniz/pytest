import xml.etree.ElementTree as ET

def gerar_relatorio_html_com_bootstrap(xml_string):
    root = ET.fromstring(xml_string)
    
    # Cabeçalho HTML com Bootstrap
    html_content = """
    <html>
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
            .table { margin-top: 20px; }
            .success { background-color: #d4edda; }
            .failure { background-color: #f8d7da; color: #721c24; }
        </style>
        <title>Relatório de Teste Pytest</title>
    </head>
    <body>
        <div class="container">
            <h1 class="text-center mt-5">Relatório de Teste Pytest</h1>
            <p class="text-center text-muted">Resumo dos testes realizados</p>
            <table class="table table-bordered table-hover">
                <thead class="thead-light">
                    <tr>
                        <th>Nome do Teste</th>
                        <th>Classe</th>
                        <th>Status</th>
                        <th>Tempo</th>
                        <th>Erro/Failure</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    for testsuite in root.findall('testsuite'):
        for testcase in testsuite.findall('testcase'):
            name = testcase.attrib['name']
            classname = testcase.attrib['classname']
            time = testcase.attrib['time']
            status = "Sucesso"
            failure_message = ""

            failure = testcase.find('failure')
            if failure is not None:
                status = "Falha"
                failure_message = failure.attrib['message'] + "\n" + failure.text
                row_class = "failure"
            else:
                row_class = "success"

            html_content += f"""
            <tr class="{row_class}">
                <td>{name}</td>
                <td>{classname}</td>
                <td>{status}</td>
                <td>{time}s</td>
                <td>{failure_message}</td>
            </tr>
            """
    
    html_content += """
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """
    
    return html_content

# Exemplo de XML de entrada
xml_input = '''<?xml version="1.0" encoding="utf-8"?>
<testsuites>
    <testsuite name="pytest" errors="0" failures="1" skipped="0" tests="1" time="0.050" timestamp="2024-10-03T14:10:41.200636-03:00" hostname="NT-500">
        <testcase classname="tests.test_qualquernome" name="test_quando_idade_for_18_entao_deve_retornar_1" time="0.001">
            <failure message="assert 0 == 1">
                def test_quando_idade_for_18_entao_deve_retornar_1():
                    entrada = 17
                    esperado = 1
                    resultado = verificar_idade(entrada)
                    assert resultado == esperado
                E       assert 0 == 1
                tests\test_qualquernome.py:12: AssertionError
            </failure>
        </testcase>
    </testsuite>
</testsuites>'''

# Gerar o HTML
html_output = gerar_relatorio_html_com_bootstrap(xml_input)

# Salvando o arquivo HTML
with open('relatorio_teste.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("Relatório HTML gerado com sucesso!")
