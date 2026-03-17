continuar = True

while continuar:
    print("")
    print("Lista de Exercícios Parte 2 - Algoritmo")
    print("1 - Conversão de Dolares para Reais")
    print("2 - Quanto ganha motorista de uber")
    print("3 - Identificar se é par ou impar")
    print("4 - Ler 10 cidades em uma unica variavel")
    print("5 - Ler 10 carros, placas e valores de diarias em uma unica variavel")

    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")
    
    match opcao:

        case "1":
            valor_dolar = float(input("Digite o valor em Dolares: "))
            cotacao_dolar = float(input("Digite a cotação do Dolar atual: "))
            valor_real = valor_dolar * cotacao_dolar
            print(f"O valor em Reais é: R${valor_real:.2f}")

        case "2":
            viagens = int(input("Digite o número de viagens realizadas hoje: "))
            print(f"O motorista de Uber ganhou R${viagens * 6.8:.2f} com as viagens realizadas.")
        
        case "3":
            num = int(input("Digite um valor: "))
            if num % 2 == 0:
                print(f"O valor {num} é par")
            else:
                print(f"O valor é impar")
        
        case "4":
            cidades = ""
            for i in range(1, 11):
              cidades = cidades + input(f"Digite o nome da cidade {i}: ") + ", "
            print("\nAs cidades informadas foram:")
            print(cidades)

        case "5":
            carros = ""
            for i in range(1, 11):
                carros = carros + "\n Carro " + input(f"Digite o nome do carro {i}: ") + ", "
                carros = carros + "Placa: " + input(f"Digite a placa do carro {i}: ") + ", "
                carros = carros + "Valor: " + "R$ " + str(float(input(f"Digite o valor da diaria do carro {i}: R$ ")))
            print("\nOs carros lidos foram:")
            print(carros)


        case _:
            print("Opção inválida.")
    
    print("")
    opcao_continuar = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_continuar == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")