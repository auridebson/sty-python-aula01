import time

def ln(x):
    print("-"*x)


cont = int(input("Digite um número para o Timer: "))

def timer(segundos):
    print(f"Contagem regressiva iniciada para {segundos} segundos.")
    
    for i in range(segundos, 0, -1):
        print(f"Tempo restante: {i} segundos")
        time.sleep(0.3)

    print("Tempo esgotado! Timer encerrado.")

timer(cont)