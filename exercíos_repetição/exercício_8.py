# Programa que gera os números inteiros no intervalo entre dois números dados
# e mostra a soma deles no final

# Recebe os dois números do usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Determina o menor e o maior número
inicio = min(num1, num2)
fim = max(num1, num2)

print(f"\nNúmeros inteiros entre {inicio} e {fim}:")

# Inicializa a variável para soma
soma = 0

# Gera e exibe os números do intervalo (excluindo os extremos)
for i in range(inicio + 1, fim):
    print(i)
    soma += i  # acumula a soma

# Exibe a soma final
print(f"\nSoma dos números: {soma}")
