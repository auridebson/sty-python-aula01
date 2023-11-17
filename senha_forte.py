def ln(x):
    print("-"*x)

esp1 = "@#$%¨&*()_+=~^;:'/"
esp2 = "0123456789"


ln(30)
senha = input("Digite uma senha forte: ")
ln(30)
securityCount = 0

for i in senha:
    if len(senha) < 6:
        print("Digite uma senha segura!\nSenha muito curta")
        break
    else:
        if i in esp1:
            securityCount += 3
            if i in esp2:
                securityCount += 1
            print(f"{senha}\nSua senha tem nota de segurança {securityCount}")

