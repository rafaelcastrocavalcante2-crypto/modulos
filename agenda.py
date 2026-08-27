import json

def listar():
    try:
        #Usam o modo 'r' (reutilizando para ler o conteúdo sem apagar o arquivo
        with open('contatos.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def adicionar(contato):
    lista = listar()
    lista.append(contato)
    #O modo 'w' apaga todo o conteúdo existente do arquivo imediatamente ao ser aberto, antes mesmo de tentar ler os dados
    with open('contatos.json', 'w', encoding='utf-8') as f:
        #Substituição de json.dumps por json.dump para gravar diretamente a estrutura de dados (lista/dicionário) no arquivo formatado
        json.dump(lista, f, indent=4, ensure_ascii=False)
    return "Adicionado"

def remover(indice):
    lista = listar()
    if 0 <= indice < len(lista):
        removido = lista.pop(indice)
        #O modo 'w' apaga todo o conteúdo existente do arquivo imediatamente ao ser aberto, antes mesmo de tentar ler os dados
        with open('contatos.json', 'w', encoding='utf-8') as f:
            #Substituição de json.dumps por json.dump para gravar diretamente a estrutura de dados (lista/dicionário) no arquivo formatado
            json.dump(lista, f, indent=4, ensure_ascii=False)
        return removido
    return "Índice inválido"

def busca_por_nome(nome):
    lista = listar()
    resultado = next((item for item in lista if item.get('nome') == nome), None)
    return resultado

# Exemplo de uso do listar
print('Listando contatos: ')
print(listar())

#incluindo novo contato
contato_novo = {"nome": "Manoel", "telefone":"11999777002","email": "rejane@email.com"}
print(adicionar(contato_novo))
print('Listando contatos atualizado: ')
print(listar())

#busca por nome
print('Listando contato encontrado pelo nome: ')
print(busca_por_nome('Rafa'))

#remover
print(remover(3))
print('Listando contatos atualizado (apos remover): ')
print(listar())

#
# [{"nome": "Ana", "telefone":"11999990000","email": "ana@email.com"},
#  {"nome": "Rafa", "telefone":"11669990000","email": "rafa@email.com"},
#  {"nome": "Cintia", "telefone":"17999990000","email": "cintia@email.com"}]
