import random

valor_aleatorio = random.randint(1,100)
acertou = False

while acertou == False:
    chute = int(input('chute um número: '))
    if chute > valor_aleatorio:
        print('chute um valor mais baixo')
    elif chute < valor_aleatorio:
        print('chute um valor mais alto')
    else:
        print('você acertou!')
        acertou = True