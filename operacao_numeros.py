# 6 - Faça um Programa que receba 2 números e em seguida pergunte ao usuário qual
# operação ele deseja realizar. O resultado da operação deve aparecer com uma frase que
# diga se o número é:

    # 4 - Faça um Programa que verifique se a letra digitada pelo usuário é vogal ou consoante.
    # 5 - Faça um programa para a leitura de quatro notas de um aluno. O programa deve calcular 
    # a média alcançada apresentar:
    # a. par ou ímpar;
    # b. positivo ou negativo;


def ln(x):
    print("-"*x)

print("Calculador Simples")
ln(30)
num1 = int(input("Digite o primeiro número da operação: "))
num2 = int(input("Digite o segundo número da operação: "))
ln(30)
print(f"\n\n")


operacao = input(f"Escolha a operação que deseja executar "
                 "\n   [ 1 ] - Adição"
                 "\n   [ 2 ] - Subtração"
                 "\n   [ 3 ] - Multiplicação"
                 "\n   [ 4 ] - Divisão"
                 "\n   [ 0 ] - SAIR"
                 "\n ")
