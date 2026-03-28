from datetime import date

continuar = True

while continuar :
    # Menu de questões
    print("")
    print("Questionário da Aula Final. Escolha uma opção: ")
    print("1 - Desconto para o dia da mulher")
    print("2 - Multas de velocidade")
    print("3 - Pode ou não votar")
    print("4 - Média de um aluno")
    print("5 - Preço de passagem")
    print("6 - Identificação de Terreno")
    print("7 - Emprestimo aceito ou negado")
    print("8 - Contagem decrescente em 5")
    print("9 - Idades")
    print("10 - Decremento usando for")
    print("11 - Soma de 7 numeros")
    print("12 - Conversao de metros")
    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")

    match opcao:
        case "1":
            nome = input("Digite o seu nome: ")
            sexo = input("Digite a letra do seu sexo: H(homem)/ M(mulher): ")
            valor = float(input("Digite o valor da compra: "))
            print("")

            if sexo.upper() == "M":
                print(f"Cliente: {nome}")
                desconto = valor * 0.13
                valor_desconto = valor - desconto
                print(f"Valor a pagar: {valor_desconto}")
            else:
                print(f"Cliente: {nome}")
                desconto = valor * 0.05
                valor_desconto = valor - desconto   
                print(f"Valor a pagar: {valor_desconto}")

        case "2":
            print("A Velocidade minima permitida é 80 Km/h")
            velocidade = int(input("Digite a velocidade do carro em Km/h: "))
            print("")

            if velocidade <= 80:
                print("Não houve multas")
            else:
                diferença_velocidade = velocidade - 80
                multa = diferença_velocidade * 5
                print(f"O valor da multa é: R$ {multa:.2f}")
        
        case "3":
            ano_atual = date.today().year
            ano_nascimento = int(input("Digite o ano que você nasceu: "))
            idade = ano_atual - ano_nascimento
            print("")

            if idade >= 18:
                print(f"Sua idade é: {idade}. Votação Obrigatória!")
            elif idade >= 16:
                print(f"Sua idade é: {idade}. Votação facultativa.")
            else:
                print(f"Sua idade é: {idade}. Não pode votar!")
        
        case "4":
            nome = input("Digite o nome do aluno: ")
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            print("")
            media = (nota1 + nota2) / 2
            if media >= 7:
                print(f"A média do aluno é: {media}. Acima da média!")
            else:
                print(f"A média do aluno é: {media}. Abaixo da média!")
        
        case "5":
            distancia = int(input("Ditancia que deseja percorrer em Km/H: "))
            print("")
            if distancia <= 200:
                preco = distancia * 0.5
                print(f"O preço da passagem nessa distancia é: R$ {preco:.2f}")
            else:
                preco = distancia * 0.45
                print(f"O preço da passagem nessa distancia é: R$ {preco:.2f}")
        
        case "6":
            largura = float(input("Digite a largura: "))
            comprimento = float(input("Digite o comprimento: "))
            area = largura * comprimento
            print("")
            if area <= 100:
                print("TERRENO POPULAR")
            elif area <= 500:
                print("TERRENO MASTER")
            else:
                print("TERRENO VIP")
        
        case "7":
            valor = float(input("Digite o valor da casa em R$: "))
            salario = float(input("Digite o salário do comprador em R$: "))
            anos = int(input("Em quantos anos irá pagar: "))
            meses_pagamento = anos * 12
            salario_30 = salario * 0.3
            prestacao = valor / meses_pagamento
            print("")

            if prestacao <= salario_30:
                print(f"Emprestimo aceito. Valor mensal de: {prestacao:.2f}")
            else:
                print("Emprestimo negado!")
        
        case "8":
            i = 100
            # for i in range(100,-1,-5):
            while i>= 0:
                print(i, end=" ")
                i -= 5
            print("Acabou!")
        
        case "9":
            continuar = True
            cont_idades = 0
            soma_idades = 0
            cont_21 = 0

            while continuar:
                idade = int(input("Digite uma idade: "))
                cont_idades += 1
                soma_idades = soma_idades + idade
                
                if idade >= 21:
                    cont_21 += 1
                opcao = input("Deseja encerrar? Digite 's' para encerrar: ")
                
                if opcao.upper() == "S":
                    break

            print("")
            print("Resultados: ")
            print(f"A quantidade de idades foi: {cont_idades}")
            print(f"A média de idades foi: {soma_idades/cont_idades}")
            print(f"Quantidade de idades maior ou igual a 21: {cont_21}")
        
        case "10":
            for i in range(100,-1,-10):
                print(i, end=" ")
            print("Acabou!")
        
        case "11":
            soma = 0
            for i in range(1,8):
                num = int(input(f"Digite o valor {i}: "))
                soma = soma + num
            print("")
            print(f"O valor da soma dos numeros é {soma}")
        
        case "12":
            distancia = float(input("Digite o valor da distancia em metros: "))
            print("")
            print("======= Resultados =======")
            print(f"Valor em KM: {distancia/1000} Km")
            print(f"Valor em HM: {distancia/100} Hm")
            print(f"Valor em Dam: {distancia/10} Dam")
            print(f"Valor em Dm: {distancia*10} Dm")
            print(f"Valor em Cm: {distancia*100} Cm")
            print(f"Valor em Mm: {distancia*1000} Mm")

        case _:
            print("Opção invalida!")
    
    print("")
    opcao_nova = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_nova == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")