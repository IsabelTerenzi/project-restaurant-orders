import csv
import os


# Requisito 1 - Implemente um método chamado
# analyze_log no módulo src/analyze_log.py que gere
# informações de uma lanchonete.
def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        # erro caso a extensão do arquivo seja inválida
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    if not os.path.isfile(path_to_file):
        # erro caso o arquivo não exista
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open(path_to_file, encoding="utf8") as arquivo:
        leitor = csv.reader(arquivo)
        pedidos = [tuple(linha) for linha in leitor]

    orders = {}

    for nome, prato, dia in pedidos:
        if nome not in orders:
            orders[nome] = {
                "hamburguer": 0,
                "coxinha": 0,
                "pizza": 0,
                "misto-quente": 0
                }
        orders[nome][prato] += 1

    # Qual o prato mais pedido por 'maria'?
    maria_prato_mais_pedido = max(orders["maria"], key=orders["maria"].get)

    # Quantas vezes 'arnaldo' pediu 'hamburguer'?
    arnaldo_qtd_hamburguer = orders["arnaldo"]["hamburguer"]

    # Quais pratos 'joao' nunca pediu?
    joao_nunca_pediu = set(prato for prato, qtd in orders["joao"]
                           .items() if qtd == 0)

    # Quais dias 'joao' nunca foi à lanchonete?
    dias = set(dia for _, _, dia in pedidos)
    joao_dias_nao_foi = dias - set(dia for nome, _, dia in pedidos
                                   if nome == "joao")

    resultado = [
        maria_prato_mais_pedido,
        arnaldo_qtd_hamburguer,
        joao_nunca_pediu,
        joao_dias_nao_foi
        ]
    resultado_formatado = "\n".join(str(valor) for valor in resultado)

    with open("arquivo.txt", "w") as file:
        file.write(resultado_formatado)
