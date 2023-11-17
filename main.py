def ln(x):
    print("-"*x)

idade = int(input("Qual o ano de seu nascimento? "))

if (2023 - idade) >= 18:
    ln(30)
    print(f"Você é maior de idade\n{2023-idade}")
    ln(30)
elif (2023 - idade) == 18:
    ln(30)
    print("Bem no limite! 18 anos")
    ln(30)
elif  (2023 - idade) <= 0:
    ln(30)
    print("ERROR:\nDigite uma idade válida")
    ln(30)
else:
    ln(30)
    print(f"MENOR DE IDADE\n{2023-idade}")
    ln(30)
    