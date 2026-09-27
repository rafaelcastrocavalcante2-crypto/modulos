try:
    class SaldoInsuficiente(Exception):
        pass

        print("------------------------------------------------")
        print("Tem um saldo de 50 reais na conta.")
        print("------------------------------------------------")
        print("Na loja tem um produto que custa 100 reais.")
        print("------------------------------------------------")

        comprar = input("Deseja comprar o produto? (s/n): ")
        valor = 100
        saldo = 50
        match comprar:
            case 's':  # Corrigido para usar a string 's' com aspas
                if valor > saldo:
            # Corrigido para colocar a mensagem entre aspas
                    raise SaldoInsuficiente("Saldo menor que o valor pedido")
            case 'n':
                print("Compra cancelada.")
            case _:
                print("Opção inválida.")
except ValueError:
    print("Entrada inválida.")