nota = float(input("Digite a nota do aluno: "))
print("")
if nota < 0 or nota > 10:
    print("Nota inválida! A nota deve ser entre 0 e 10.")
elif nota < 6:
    print("Aluno reprovado.")
elif nota < 7:
    print("Aluno em recuperação.")
else:
    print("Aluno aprovado.")