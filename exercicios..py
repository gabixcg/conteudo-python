nm_1 = int(input("digite o valor da nota: "))
nm_2 = int(input("digite o valor da nota: "))
nm_3 = int(input("digite o valor da nota: "))
nm_4 = int(input("digite o valor da nota: "))

media = nm_1 + nm_2 + nm_3 + nm_4

if media >= 7:
    print("aprovado")
elif media >= 3:
    print("em exame")
else :
    print("reprovado")