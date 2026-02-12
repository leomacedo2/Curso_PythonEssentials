continuar = True

while continuar:
    print("")
    print("Aplicando Lógica com JS(C) - Terceira lista")
    print("1 - Ler 10 numeros inteiros e exibir a soma de todos")
    print("2 - Formulário de aprovação de aluno")
    print("3 - Promoção de salário")
    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")
    match opcao:

        case "1":
            soma = 0
            for i in range(10):
                numero = int(input(f"Digite o {i+1}º número inteiro: "))
                soma += numero
            print(f"A soma dos números é: {soma}")

        case "2":
            nome = input("Digite o nome do aluno: ")
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            media = (nota1 + nota2) / 2
            print("")
            print(f"Aluno: {nome}")
            print(f"Média: {media}")
            if media >= 6:
                print(f"Situação: Aprovado")
            else:
                print(f"Situação: Reprovado")

        
        case "3":
            salario_atual = float(input("Digite o salário atual: "))
            if salario_atual < 1500:
                aumento = salario_atual * 0.50
            elif 1500 <= salario_atual < 4300:
                aumento = salario_atual * 0.40
            else:
                aumento = salario_atual * 0.30
            salario_novo = salario_atual + aumento
            print(f"Salário atual: R${salario_atual:.2f}")
            print(f"Aumento: R${aumento:.2f}")
            print(f"Salário novo: R${salario_novo:.2f}")

        case _:
            print("Opção inválida.")
    
    print("")
    opcao_continuar = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_continuar == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")
