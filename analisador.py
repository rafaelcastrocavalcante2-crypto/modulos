print("----------------------------------------------------------------")
frase = input("Digite a frase: ")
vogais = 0
consoantes = 0
for letra in frase:
    if letra in 'aeiou':
        vogais += 1
    elif letra.isalpha():
        consoantes += 1
print("----------------------------------------------------------------")
print(f'Sua frase tem {vogais} de vogais e {consoantes} de consoantes')
print("----------------------------------------------------------------")