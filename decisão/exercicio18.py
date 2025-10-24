preco_alcool = 4.17
preco_gasolina = 6.29

qtd_litros = float(input("digite a quantidade de litros:"))
tipo = input("digite o tipo de combustível( A - alcool, G - gasolina): ")

desconto = 0

if tipo == "A":
    if qtd_litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    preco_litro = qtd_litros * preco_alcool
    preco_total = preco_litro - (preco_litro * desconto)
elif tipo == "G" :
    if qtd_litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco_litro = qtd_litros * preco_gasolina
    preco_total = preco_litro - (preco_litro * desconto)

if preco_total > 0:
    print("o valor a pagar é:", preco_total)