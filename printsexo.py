def ln(x):
    print("-"*x)


# Feminimo - F
# Masculino - M

sexo = input("Digite o seu sexo.\n   [M] - Masculino\n   [F] - Feminino\n")

if sexo.upper() == 'M':
    ln(30)
    print("Sexo: Masculino escolhido")
    ln(30)
elif sexo.upper() == 'F':
    ln(30)
    print("Sexo: Feminino escolhido")
    ln(30)
else:
    ln(30)
    print("ERROR:\nSexo Inválido!")
    ln(30)

