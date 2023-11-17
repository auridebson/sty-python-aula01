def ln(x):
    print("-"*x)

print ('Digite dois números para verificar qual maior deles')
ln(50)

num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))

resultado = 0

if num1 > num2:
    resultado = num1
    print(f'O maior número é {resultado}')
elif num2 > num1:
    resultado = num2
    print(f'O maior número é {resultado}')
else:
    resultado = 'Iguais'
    print(f'Os números são iguais.')

