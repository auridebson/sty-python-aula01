def ln(x):
    print("-"*x)

numero = int(input("Digite o número para forma a tabuada: "))


for i in range(11):
    print(f"{i} x {numero} = {i*numero}  |  {i} + {numero} = {i+numero}  |  {i} - {numero} = {i-numero}  |  {i} / {numero} = {i/numero}  |  ")