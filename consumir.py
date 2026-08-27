import requests

print("#############################")
print("### consulta cep ##")
print("#############################")

cep_input = input("Digite o cep para a consulta: ")

if len (cep_input) != 8:
    print("Quantidade de caracteres invalidas")
    exit()
else:
    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_input))

address_data = request.json()

if 'erro' not in address_data:
    print(request.json())
else:
   print("Cep invalido")