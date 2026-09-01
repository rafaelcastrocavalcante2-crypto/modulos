import requests
import json


def buscar_cep(cep):

    if cep.isdigit():
        print("CEP valido")
    else:
        return "CEP invalido"

    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    print(f'Erro da API: {resposta.status_code}')
    if resposta.status_code == 200:
           endereco  = resposta.json()           
    else:
          endereco = 'CEP nao encontrado'

    return endereco

    
print("CEP - Consulta API")
cep_input = input("Digite o CEP para a consulta: ")
endereco = buscar_cep(cep_input)
print(endereco)
    