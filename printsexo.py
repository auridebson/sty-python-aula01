def ln(x):
    print("-"*x)


# Feminimo - F
# Masculino - M

sexo = input("Digite o seu sexo.\n[M] - Masculino\n[F] - Feminino\n")

if sexo.upper() == 'M':
    print("Sexo: Masculino escolhido")
elif sexo.upper() == 'F':
    print("Sexo: Feminino escolhido")
else:
    print("ERROR:\nSexo Inválido!")

