fim = False

while fim == False:
    nome = str(input("Nome do aluno: "))
    nota1 = float(input("Nota p1: "))
    nota2 = float(input("Nota p2: "))

    lista_notas = [nota1, nota2]

    def calcular_media(notas):
        return sum(notas) / len(notas)

    def verificar_situacao(media_final):
        if media_final >= 7.0:
            print("Aprovado")
        else:
            print("Reprovado")

    media_aluno = calcular_media(lista_notas)
    print(f"Média: {media_aluno}")
    verificar_situacao(media_aluno)
    final = input("Fim?: ")
    match final:
        case "fim":
            fim = True
        case _:
            fim = False