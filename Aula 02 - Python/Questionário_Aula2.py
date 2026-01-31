
opcao = ""

while opcao != "0":
    # Menu de questões
    print("")
    print("Questionário da Aula 2. Escolha uma opção: ")
    print("1 - Comparação de dois inteiros")
    print("2 - Sua idade é?")
    print("3 - O proximo e o anterior de um numero")
    print("4 - Salário total com o valor da hora a R$:51,90")
    print("5 - O quadrado de um numero")
    print("6 - Calculo solicitanto base e potencia")
    print("7 - Idade se pode dirigir")
    print("8 - Nome do cliente e desconto de 15%")
    print("9 - Aprovação de aluno")
    print("10 - Numero par ou impar?")
    print("11 - Requisição de senha")
    print("12 - Aposentado ou Trabalho Formal?")
    print("13 - Calculo de desconto de 20%")
    print("14 - Seleção recrutamento de menores")
    print("15 - Variaveis booleanas")
    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")

    match opcao:
        case "1":
            inteiro1 = int(input("Qual o primeiro numero? "))
            inteiro2 = int(input("Qual o segundo numero? "))
            print("")

            if inteiro1 > inteiro2 :
                print(f"{inteiro1} é maior que {inteiro2}")
            elif inteiro2 > inteiro1 :
                print(f"{inteiro2} é maior que {inteiro1}")
            else :
                print(f"{inteiro1} e {inteiro2} são iguais")

        case "2":
            ano = int(input("Digite seu ano de nascimento: "))
            print("")
            idade = 2026 - ano
            print(f"A sua idade no final desse ano será: {idade}")



        case "3":
            inteiro = int(input("Digite um numero inteiro "))
            print("")
            print(f"O numero anterior a {inteiro} é {inteiro-1}")
            print(f"O numero sucessor a {inteiro} é {inteiro+1}")



        case "4":
            horas = float(input("Quantas horas você trabalhou? "))
            print("")

            resultado = horas*51.90
            #Para mostrar o valor com duas casas decimais se coloca no resultado :.2f
            print(f"Seu salário é: R$ {resultado:.2f}")


        case "5":
            num = int(input("Digite um numero "))
            print("")
            print(f"O quadrado desse numero é {num*num}")

        
        case "6":
            base = int(input("Digite a base "))
            potencia = int(input("Digite a potencia "))
            print("")
            print(f"O resultado é: {base**potencia}")

        
        case "7":
            idade = int(input("Digite sua idade "))
            print("")
            if idade >= 18:
                print("Habilitada para dirigir")
            else:
                print("Não habilitada para dirigir")
        
        
        case "8":
            nome = input("Digite o nome do cliente ")
            compra = float(input("Digite o valor total da compra: R$ "))
            print("")

            compra = compra - compra*0.15

            print(f"O cliente {nome} ganhou um desconto!")
            print(f"O valor total com o desconto ficou: R$ {compra:.2f}")

        
        case "9":
            nota1 = float(input("Digite a primeira nota "))
            nota2 = float(input("Digite a segunda nota "))
            nota3 = float(input("Digite a terceira nota "))
            print("")

            media = (nota1 + nota2 + nota3)/3

            if media >= 7:
                print("Aluno Aprovado")
            else:
                print("Aluno Reprovado")

        
        case "10":
            inteiro = int(input("Digite um numero inteiro "))

            if inteiro % 2 == 0 :
                print(f"O numero {inteiro} é par")
            else :
                print(f"O numero {inteiro} é impar")

        
        case "11":
            senha_segura = "546987A"

            senha_digitada = input("Digite a senha de segurança: ")
            print("")

            if senha_segura == senha_digitada:
                print("Senha aprovada")
            else:
                print("Senha não aprovada")

        
        case "12":
            idade = int(input("Qual é a sua idade? "))

            if idade >= 60:
                print("Aposentado")
            else: 
                print("Trabalho Formal")


        case "13":
            valor_total = float(input("Digite o valor da compra: R$ "))
            fidelidade = input("O Cliente tem cartão fidelidade? Digite sim ou nao : ")

            valor_total_descontado = valor_total - valor_total*0.20

            if (valor_total > 500 or fidelidade == "sim"):
                print(f"Você ganhou desconto! O preço será: R$ {valor_total_descontado:.2f} ")
            else:
                print(f"Valor sem desconto! {valor_total:.2f}")

        
        case "14":
            ensino_medio = input("O usuário está cursando ensino médio? Digite sim ou nao : ")
            idade = int(input("Qual a idade do usuario? "))

            if (idade <=18 and ensino_medio == "sim"):
                print("Aprovado para próxima fase")
            else: 
                print("Não atende aos critérios")
        
        case "15":
            crachaAtivo = True
            senhaCorreta = True

            if (crachaAtivo and senhaCorreta):
                print("Acesso liberado")
            else:
                print("Acesso negado")
        
        case _:
            print("Opção invalida!")
    
    print("")
    opcao_nova = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_nova == "n":
        opcao = "0"
        print("")
        print("Obrigado!")
        print("")
    