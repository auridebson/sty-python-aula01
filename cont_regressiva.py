def ln(x):
    print("-"*x)


cont = int(input("Digite um número para o Timer: "))

while True:
    if cont >= 0:
        print(f"Contando - {cont}")
        cont = cont - 1
    else:
        print("Final da contagem")
        break