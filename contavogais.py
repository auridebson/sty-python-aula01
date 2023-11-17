def ln(x):
    print("-"*x)


vogais = 'aeiou'
frase = input("Digite uma frase pra contagem de vogais: ")
contagem = 0

for i in frase:
    if i in vogais:
        print(f"{i} encontrado na frase")
        contagem += 1

print(f"Foram encontradas {contagem} vogais na frase")
