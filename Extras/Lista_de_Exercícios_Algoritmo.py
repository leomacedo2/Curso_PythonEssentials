import datetime
from datetime import datetime

continuar = True

while continuar:
    print("")
    print("Lista de Exercícios - Algoritmo")
    print("1 - Atribuição de variáveis")
    print("2 - Calculadora simples")
    print("3 - Consumo de um carro")
    print("4 - Reprovação por falta")
    print("5 - Quantos anos a pessoa tem informando apenas o ano?")
    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")
    
    match opcao:

        case "1":
            nome = "Leo"
            idade = 34
            altura = 1.75
            print(f"Nome: {nome}")
            print(f"Idade: {idade} anos")
            print(f"Altura: {altura} metros")

        
        case "2":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"A soma de {num1} e {num2} é: {num1 + num2:.2f}")
            print(f"A subtração de {num1} e {num2} é: {num1 - num2:.2f}")
            print(f"A multiplicação de {num1} e {num2} é: {num1 * num2:.2f}")
            if num2 != 0:
                print(f"A divisão de {num1} por {num2} é: {num1 / num2:.2f}")
            else:
                print("Divisão por zero não é permitida.")
        

        case "3":
            distancia = float(input("Digite a distância percorrida (em km): "))
            combustivel = float(input("Digite a quantidade de combustível consumida (em litros): "))
            if combustivel != 0:
                consumo = distancia / combustivel
                print(f"O consumo do carro é: {consumo:.2f} km/l")
            else:
                print("Quantidade de combustível não pode ser zero.")


        case "4":
            aluno = input("Digite o nome do aluno: ")
            horas_mes = int(input("Digite a quantidade de horas letivas no mês: "))
            if horas_mes > 0:
                horas_faltas = int(input("Digite a quantidade de horas que o aluno faltou no mês: "))
                percentual_faltas = (horas_faltas / horas_mes) * 100 
                if percentual_faltas > 25:
                    print(f"O aluno {aluno} foi reprovado por falta. Percentual de faltas: {percentual_faltas:.2f}%")
                else:
                    print(f"O aluno {aluno} não foi reprovado por falta. Percentual de faltas: {percentual_faltas:.2f}%")
            else:
                print("Quantidade de horas letivas no mês não pode ser zero nem negativa.") 


        case "5": 
            nome = input("Digite o nome da pessoa: ")
            ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
            ano_atual = datetime.now().year
            idade = ano_atual - ano_nascimento
            print(f"{nome} tem {idade} anos.")

        case _:
            print("Opção inválida.")
    
    print("")
    opcao_continuar = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_continuar == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")