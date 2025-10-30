import math

a = float(input("digite o valor de A:"))
b = float(input("digite o valor de B:"))
c = float(input("digite o valor de C:"))

if a == 0:
    print("não é uma equação de segundo grau")
    exit(1)

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Delta:",delta)
    print("não é possivel calcular raiz de numeros nagativos")
    exit(1)

if delta == 0:
    x = (b * -1) / (2 * a)
    print(f"o valor de X é {x}")
else:
    raiz = math.sqrt(delta)
    xa = ((b * -1) + raiz) / (2 * a)
    xb = ((b * -1) - raiz) / (2 * a)
    print(f"o valor de x' é {xa}")
    print(f"o valor de x'' é {xb}")