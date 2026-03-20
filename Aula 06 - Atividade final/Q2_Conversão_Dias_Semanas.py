dias = int(input("Digite a quantidade de dias: "))
semanas = dias // 7 # Operador de divisão inteira!
dias_restantes = dias % 7
print("")
print(f"{dias} dias equivalem a {semanas} semana(s) e {dias_restantes} dia(s).")