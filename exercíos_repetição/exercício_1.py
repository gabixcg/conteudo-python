while True:
    nota = float(input("Digite uma nota entre 0 a 10:"))

    if 0 <= nota <= 10:
        print("Nota válida: Obrigado.")
        break
    else:
        print("Nota inválido! Tente novamente.")