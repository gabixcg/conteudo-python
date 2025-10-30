while True:
    print("\n--- Comparador de Crescimento Populacional ---")

    # Entrada com validação
    try:
        pop_a = int(input("Informe a população inicial do país A: "))
        pop_b = int(input("Informe a população inicial do país B: "))
        taxa_a = float(input("Informe a taxa de crescimento anual do país A (em %): "))
        taxa_b = float(input("Informe a taxa de crescimento anual do país B (em %): "))

        # Validação de valores positivos
        if pop_a <= 0 or pop_b <= 0 or taxa_a < 0 or taxa_b < 0:
            print("❌ Erro: todas as populações e taxas devem ser positivas.")
            continue

        # Conversão de porcentagem para decimal
        taxa_a /= 100
        taxa_b /= 100

    except ValueError:
        print("❌ Erro: digite apenas números válidos.")
        continue

    # Cálculo do tempo necessário
    anos = 0
    pop_a_temp = pop_a
    pop_b_temp = pop_b

    if pop_a >= pop_b:
        print("\nO país A já possui população maior ou igual à do país B.")
    else:
        while pop_a_temp < pop_b_temp:
            pop_a_temp += pop_a_temp * taxa_a
            pop_b_temp += pop_b_temp * taxa_b
            anos += 1

        print(f"\n✅ A população do país A ultrapassará ou igualará país B em {anos} anos.")
        print(f"Após {anos} anos:\n"
              f" - País A: {pop_a_temp:.0f} habitantes\n"
              f" - País B: {pop_b_temp:.0f} habitantes")

    # Perguntar se o usuário quer repetir
    repetir = input("\nDeseja realizar outro cálculo? (s/n): ").strip().lower()
    if repetir != 's':
        print("\nEncerrando o programa. Até logo! 👋")
        break

