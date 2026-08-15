fim = False
lista_notas = []

nome = str(input("Nome do aluno: "))

while fim == False:  
    entrada = input("Digite a nota da prova: ")
    if entrada != "fim" :
        nota = float(entrada)
        lista_notas.append(nota)
    else:
        fim = True;  


def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(media_final):
    if media_final >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"

#calcular a media das notas do aluno
media_aluno = calcular_media(lista_notas)
print(f"Média: {media_aluno}")
#valida a situacao do aluno
situacao = verificar_situacao(media_aluno)

#divulga o resultado do aluno
print(f"O aluno: {nome} foi {situacao} com a média {media_aluno}")
