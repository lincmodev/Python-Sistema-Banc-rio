# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal
# TODO: Retorne o plano de internet adequado:
    resultado = ''
    if consumo <= 10.0:
      resultado = "Plano Essencial Fibra - 50Mbps"
    elif consumo > 10.0 and consumo <= 20.0:
      resultado = "Plano Prata Fibra - 100Mbps"
    elif consumo > 20:
      resultado = "Plano Premium Fibra - 300Mbps"
    return resultado


# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))