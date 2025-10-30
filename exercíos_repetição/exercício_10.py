# Solicita os números ao usuário
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# Inicializa o resultado
resultado = 1

# Caso o expoente seja positivo
if expoente > 0:
    for i in range(expoente):
        resultado *= base
# Caso o expoente seja zero
elif expoente == 0:
    resultado = 1
# Caso o expoente seja negativo
else:
    for i in range(-expoente):
        resultado *= base
    resultado = 1 / resultado

# Exibe o resultado
print(f"{base} elevado a {expoente} é {resultado}")
