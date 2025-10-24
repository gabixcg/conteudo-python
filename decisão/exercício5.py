#A
nm_1 = int(input("digite o valor da nota: "))
nm_2 = int(input("digite o valor da nota: "))

media = (nm_1 + nm_2) /  2
print("a media do aluno",media)
if media >= 7:
    print("o aluno está aprovado")

#B
elif media <7:
    print("o aluno está reprovado")

#C
if media ==10:
    print("o aluno é um aluno destaque")
