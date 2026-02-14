continuar = True

while continuar:
    print("")
    print("Aplicando Lógica com JS(C) - Terceira lista")
    print("1 - Ler 10 numeros inteiros e exibir a soma de todos")
    print("2 - Formulário de aprovação de aluno")
    print("3 - Promoção de salário")
    print("4 - Idade de um nadador e definir a categoria")
    print("5 - Refrigerantes Meia-Cola")
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


        case "4":
            idade = int(input("Digite a idade do nadador: "))
            if 5 <= idade <= 7:
                categoria = "Infantil A"
            elif 8 <= idade <= 10:
                categoria = "Infantil B"
            elif 11 <= idade <= 13:
                categoria = "Juvenil A"
            elif 14 <= idade <= 17:
                categoria = "Juvenil B"
            elif idade >= 18:
                categoria = "Adulto"
            else:
                categoria = "Sem categoria"
            print("")
            print(f"Idade: {idade} anos")
            print(f"Categoria: {categoria}")

        
        case "5":
            lata = int(input("Digite a quantidade de latas de 350 ml foram compradas:"))
            garrafa = int(input("Digite a quantidade de garrafas de 600 ml foram compradas:"))
            garrafao = int(input("Digite a quantidade de garrafões de 2 litros foram comprados:"))
            total_litros = (lata * 0.35) + (garrafa * 0.6) + (garrafao * 2)
            print("")
            print(f"Total de litros de refrigerante: {total_litros:.2f} litros")


        case _:
            print("Opção inválida.")
    
    print("")
    opcao_continuar = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_continuar == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")
