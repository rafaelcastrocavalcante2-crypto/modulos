try:
    celsius = input("Digite a temperatura em Celsius: ")
    valor = int(celsius)
    fahrenheit: int = valor * 9 / 5 + 32
    print("------------------------------------------------")
    print(f'A temperatura em fahrenheit é {fahrenheit}')
    print("------------------------------------------------")
except ValueError:
    certo = False
    while certo == False:
            try:
                celsius = input("Digite a temperatura em Celsius: ")
                valor = float(celsius)
                fahrenheit: float = valor * 9 / 5 + 32
                print("------------------------------------------------")
                print(f'A temperatura em fahrenheit é {fahrenheit}')
                print("------------------------------------------------")
            except ValueError:
                print("------------------------------------------------")
                print("Erro: Por favor, digite apenas números.")
                print("------------------------------------------------")
            else:
                certo = True
                print("------------------------------------------------")
                print("Entrada aceita com sucesso.")
                print("------------------------------------------------")
    print("------------------------------------------------")
    print("Por favor, digite um número válido.")
    print("------------------------------------------------")
else:
    print("Entrada aceita com sucesso.")
    print("------------------------------------------------")
finally:
    print("Fim da tentativa.")
    print("------------------------------------------------")