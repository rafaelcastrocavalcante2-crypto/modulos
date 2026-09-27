import json
try:
    class Contato:
        def __init__(self, nome, telefone, email):
            self.nome = nome
            self.telefone = telefone
            self.email = email
            return self
        
    class ContatoProfissional(Contato):
        def __init__(self, nome, telefone, email, empresa):
            super().__init__(nome, telefone, email)
            self.empresa = empresa
            return self
    class ContatoPessoal(Contato):
        def listar():
            try:
                #Usam o modo 'r' (reutilizando para ler o conteúdo sem apagar o arquivo
                with open('contatos.json', 'r', encoding='utf-8') as f:
                    return json.load(f)
            except FileNotFoundError:
                    return []
    class adicionar(Contato):
        def adicionar(contato):
            lista = ContatoPessoal.listar()
            lista.append(contato)
            #O modo 'w' apaga todo o conteúdo existente do arquivo imediatamente ao ser aberto, antes mesmo de tentar ler os dados
            with open('contatos.json', 'w', encoding='utf-8') as f:
            #Substituição de json.dumps por json.dump para gravar diretamente a estrutura de dados (lista/dicionário) no arquivo formatado
                json.dump(lista, f, indent=4, ensure_ascii=False)
            return "Adicionado"
        
    class remover(Contato):
        def remover(indice):
            lista = ContatoPessoal.listar()
            if 0 <= indice < len(lista):
                removido = lista.pop(indice)
                #O modo 'w' apaga todo o conteúdo existente do arquivo imediatamente ao ser aberto, antes mesmo de tentar ler os dados
                with open('contatos.json', 'w', encoding='utf-8') as f:
                    #Substituição de json.dumps por json.dump para gravar diretamente a estrutura de dados (lista/dicionário) no arquivo formatado
                    json.dump(lista, f, indent=4, ensure_ascii=False)
                return removido
            return "Índice inválido"
    class busca_por_nome(Contato):
        def busca_por_nome(nome):
            lista = ContatoPessoal.listar()
            resultado = next((item for item in lista if item.get('nome') == nome), None)
            return resultado

    # Exemplo de uso do listar
    print('Listando contatos: ')
    print(ContatoPessoal.listar())

    #incluindo novo contato
    contato_novo = {"nome": "Manoel", "telefone":"11999777002","email": "rejane@email.com"}
    print(adicionar.adicionar(contato_novo))
    print('Listando contatos atualizado: ')
    print(ContatoPessoal.listar())

    #busca por nome
    print('Listando contato encontrado pelo nome: ')
    print(busca_por_nome.busca_por_nome('Rafa'))

    #remover
    print(remover.remover(3))
    print('Listando contatos atualizado (apos remover): ')
    print(ContatoPessoal.listar())
except ValueError:
    print("Erro: não conseguimos carregar os contatos.")
#
# [{"nome": "Ana", "telefone":"11999990000","email": "ana@email.com"},
#  {"nome": "Rafa", "telefone":"11669990000","email": "rafa@email.com"},
#  {"nome": "Cintia", "telefone":"17999990000","email": "cintia@email.com"}]
