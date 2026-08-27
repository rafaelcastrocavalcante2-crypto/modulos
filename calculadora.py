import sys
operações = {
    '+': "somar",
    '-': "subtrair",
    '*': "multiplicar",
    '/': "dividir",
}

numero1 = int(input("Digite o número: "))
sys.stdout.write("----------------------------------------------------\n")
numero2 = int(input("Digite o número: "))
sys.stdout.write("----------------------------------------------------\n")
operação = input("Qual operação deseja usar?: ")
match operação:
    case "+":
        sys.stdout.write(f"Resultado: {int(numero1) + int(numero2)}\n")
    case "-":
        sys.stdout.write(f"Resultado: {int(numero1) - int(numero2)}\n")
    case "/":
        sys.stdout.write(f"Resultado: {int(numero1) / int(numero2)}\n")
    case "*":
        sys.stdout.write(f"Resultado: {int(numero1) * int(numero2)}\n")