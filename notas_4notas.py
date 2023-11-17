# 5
# Faça um programa para a leitura de quatro notas de um aluno. O programa deve calcular a
# média alcançada apresentar:
# a. par ou ímpar;
# b. positivo ou negativo;
# a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# b. A mensagem "Reprovado" , se a média for menor do que sete;
# c. A mensagem "Aprovado com Distinção", se a média for igual a dez.

def ln(x):
    print("-"*x)


nmAluno = input("Digite o nome do Aluno: ")
notas = []


while len(notas) < 4:
    notas += input(f"Digite a nota do aluno {nmAluno}: ")

print(notas)


