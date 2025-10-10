area_pintar = float(input("digite quantos metros sarão pintados:" ))
l_necesario = area_pintar / 3
lata_tinta = (l_necesario/ 18)
val = lata_tinta * 80
print("você deverá comprar",round(lata_tinta,2), "que ira sair no valor de R$",round(val,2))
