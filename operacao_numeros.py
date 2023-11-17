# 6 - Faça um Programa que receba 2 números e em seguida pergunte ao usuário qual
# operação ele deseja realizar. O resultado da operação deve aparecer com uma frase que
# diga se o número é:
    # a. par ou ímpar;
    # b. positivo ou negativo;


def ln(x):
    print("-"*x)

print("Calculador Simples")
ln(30)
x = int(input("Digite o primeiro número da operação: "))
y = int(input("Digite o segundo número da operação: "))
ln(30)
print(f"\n\n")


operacao = input(f"Escolha a operação que deseja executar "
                 "\n   [ 1 ] - Adição"
                 "\n   [ 2 ] - Subtração"
                 "\n   [ 3 ] - Multiplicação"
                 "\n   [ 4 ] - Divisão"
                 "\n   [ 0 ] - SAIR"
                 "\n ")


match operacao:
    case 1:
        resultado = x + y
        print(resultado)
    case 2:
        resultado = x - y
        print(resultado)
    case 3:
        resultado = x * y
        print(resultado)
    case 4:
        resultado = x / y
        print(resultado)
    case 0:
        print("Saindo do programa...")

# FINALIZAR EM CASA