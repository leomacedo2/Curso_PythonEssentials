base = int(input("Digite o salário base do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
horas_extras_valor = int(input("Digite a quantidade de horas extras trabalhadas: "))
valor_hora = base / horas_trabalhadas
valor_hora_extra = valor_hora * 1.5 #50%
salario_final = base + (horas_extras_valor * valor_hora_extra)
print("")
print(f"O salário final do funcionário é: R${salario_final:.2f}")
