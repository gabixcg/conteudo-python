salario_bruto = float(input("digite o valor do salário: "))
horas_trabalhadas = float(input("digite o tanto de horas trabalhadas:" ))

valor_hora = salario_bruto / horas_trabalhadas

print("o valor que o funcionario ganha por hora é igual a:", valor_hora)

#Atividade A

salario_bruto = valor_hora * horas_trabalhadas
print("o salario bruto sera igual a:", salario_bruto)

#Atividade B

pagou_INSS = salario_bruto * 0.08
print("o valor que sera pago é:", pagou_INSS)

#Atividade C

pagou_sindicato = salario_bruto * 0.05
print("o valor que sera pago é: ", pagou_sindicato)

#Atividade D
salario_liquido = salario_bruto - pagou_INSS - pagou_sindicato
print("o salario liquido sera de:",salario_liquido)
