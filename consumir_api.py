import requests
import json


def buscar_cep(cep):
    retorno = ''
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    print(f'Erro da API: {resposta.status_code}')
    if resposta.status_code == 200:
           retorno  = resposta.json()           
    else:
          return 'CEP nao encontrado'
    endereco = ''
    try:
        with open(retorno, 'r', encoding='utf-8') as f:
            endereco = json.load(f)
    except FileNotFoundError:
        endereco = 'Endereco nao encontrado'
    return
    

print("CEP - Consulta API")
cep_input = input("Digite o cep para a consulta: ")
print(buscar_cep(cep_input))
    