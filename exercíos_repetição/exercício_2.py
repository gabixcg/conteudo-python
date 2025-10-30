# Programa para validar informações do usuário

# Valida nome
while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("Erro: o nome deve ter mais de 3 caracteres.")

# Valida idade
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        else:
            print("Erro: a idade deve estar entre 0 e 150.")
    except ValueError:
        print("Erro: digite um número válido para a idade.")

# Valida salário
while True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario > 0:
            break
        else:
            print("Erro: o salário deve ser maior que zero.")
    except ValueError:
        print("Erro: digite um valor numérico para o salário.")

# Valida estado civil
while True:
    estado_civil = input("Digite seu estado civil (s - solteiro(a), c - casado(a), v - viúvo(a), d - divorciado(a)): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Erro: estado civil deve ser 's', 'c', 'v' ou 'd'.")

# Exibe as informações válidas
print("\nInformações válidas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Estado Civil: {estado_civil}")
