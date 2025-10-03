# Arquivo para aprender a relizar cálculos com Phyton

# Sinais matemáticos:
# + Soma                    Serve para somar valores
# - Subtração               Serve para diminur um valor do outro
# * Multiplicação           Serve para multiplicar valores
# / Divisão                 Serve para dividir um valor para outro
# ** Potência               Serve para fazer  potência de valores
# // Divisão inteira        Serve para retornar a parte inteira de valores
# % Resto de divisão        Serve para retornar o resto da divisão

numero_1 = int(input("Digite o primeiro valor: "))
numero_2 = int(input("Digite o segundo valor: "))

resultado = numero_1 + numero_2
print("A soma do numero 1 com o numero 2 é: ",resultado)

resultado = numero_1 - numero_2
print("A subtração do numero 1 pelo numero 2 é: ",resultado)

resultado = numero_1 * numero_2
print("A multiplicação do numero 1 pelo numero 2 é: ",resultado)

resultado = numero_1 / numero_2
print("A divisão do numero 1 pelo numero 2 é:",resultado)

resultado = numero_1 ** numero_2
print("A potência do numero 1 pelo numero 2 é:",resultado)

resultado = numero_1 // numero_2
print("A divisão inteira do numero 1 pelo numero 2 é:",resultado)

resultado = numero_1 % numero_2
print("O resto de divisao do numero 1 pelo numero 2 é:",resultado)