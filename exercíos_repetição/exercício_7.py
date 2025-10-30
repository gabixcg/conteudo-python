# Programa que gera os números inteiros no intervalo entre dois números dados

# Recebe os dois números do usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Determina o menor e o maior número
inicio = min(num1, num2)
fim = max(num1, num2)

print(f"\nNúmeros inteiros entre {inicio} e {fim}:")

# Gera e exibe os números do intervalo (excluindo os extremos)
for i in range(inicio + 1, fim):
    print(i)
