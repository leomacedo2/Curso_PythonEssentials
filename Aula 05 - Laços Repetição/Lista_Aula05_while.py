continuar = True
while continuar :
    # Menu de questões
    print("")
    print("Questionário da Aula 5. Laço de repetição 'while'. Escolha uma opção: ")
    print("1 - Ler numeros até o usuario digitar um valor negativo")
    print("2 - Lendo notas de alunos enquanto ela for valida (entre 0 e 10)")
    print("3 - Numeros pares menores que um numero")
    print("4 - Ler valores enquanto a soma for menor que 100")
    print("5 - Ler senhas até a senha correta")
    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")

    match opcao:

        case "1":
            num = 0
            while num >= 0:
                num = int(input("Digite um numero (digite um valor negativo para encerrar): "))
                if num >= 0:
                    print(f"Você digitou: {num}")
                else:
                    print("Valor negativo digitado. Encerrando o programa.")

        case "2":
            nota = 0
            while nota >= 0 and nota <= 10:
                nota = float(input("Digite uma nota entre 0 e 10: "))
                if nota < 0 or nota > 10:
                    print("Nota inválida. Programa encerrado.")
                else:
                    print(f"Nota de aluno: {nota:.2f}")
        
        case "3":
            numero = int(input("Digite um numero: "))
            numero -= 1
            print("")
            print("Os numeros pares menores que esse numero são: ")
            while numero >= 0:
                if numero % 2 == 0:
                    print(numero)
                numero -= 1
        
        case "4":
            continua = True
            while  continua:
                num1 = float(input("Digite um valor: "))
                num2 = float(input("Digite outro valor: "))
                soma = num1+num2
                print("")
                print(f"A soma dos valores é: {soma}")
                print("")
                if soma < 100:
                    print("A soma foi menor que 100 então o programa encerrou")
                    continua = False

        case "5":
            senha = 0
            while senha != "1234":
                senha = input("Digite a senha: ")
                if senha != "1234":
                    print("Senha incorreta. Tente novamente.")
            print("Senha correta! Obrigado")

            
        case _:
            print("Opção invalida!")
    
    print("")
    opcao_nova = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_nova == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")