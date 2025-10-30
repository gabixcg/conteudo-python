# Gerador de Tabuada

# Solicita ao usuário um número entre 1 e 10
numero = int(input("Digite um número entre 1 e 10 para ver a tabuada: "))

# Verifica se o número está dentro do intervalo permitido
if 1 <= numero <= 10:
    print(f"\nTabuada do {numero}:")
    print("-" * 15)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    print("-" * 15)
else:
    print("Por favor, digite um número entre 1 e 10.")

