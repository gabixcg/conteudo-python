peso_peixes = float(input("qual é o peso da sua carga: "))
peso_maximo = 50.0
valor_multa = 4


if peso_peixes > peso_maximo:
    execesso = peso_peixes - peso_maximo
    multa = execesso * valor_multa
    print("peso maximo excedido por", execesso)
    print("sua multa é R$", multa)
else:
    print("você não passou do limite de peso permitido")
