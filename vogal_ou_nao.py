# 4
# Faça um Programa que verifique se a letra
# digitada pelo usuário é vogal ou consoante.

def ln(x):
    print("-"*x)

vogal = ['a','e','i','o','u']
numeros = [0,1,2,3,4,5,6,7,8,9]
consoantes = ['b','c','d','f','g','h','j','l','m','n','n','p','q','r','s','t','v','x','z','w','y']

caractere = input("Digite uma letra para verificação: ")

tamanhoChar = len(caractere)

if tamanhoChar > 1 or tamanhoChar == 0:
      ln(15)
      print(f"Você digitou {tamanhoChar} caracteres.\nDigite um caractere somente para validação.")
      ln(15)
else:
    #   Código depois de verificar tamanho da entrada
    if caractere in vogal:
        ln(30)
        print("Seu caractere é uma VOGAL")
        ln(30)

    elif caractere in consoantes:
        ln(30)
        print("Seu caractere não é uma VOGAL\nEsse caractere é uma consoante!")
        ln(30)

    elif int(caractere) in numeros:
            ln(30)
            print("Seu caractere é um NÚMERO")
            ln(30)
    else:
            ln(30)
            print("Digite somente um caractere!")
            ln(30)