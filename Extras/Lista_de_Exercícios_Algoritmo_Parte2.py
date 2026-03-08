continuar = True

while continuar:
    print("")
    print("Lista de Exercícios Parte 2 - Algoritmo")
    print("1 - Conversão de Dolares para Reais")
    print("2 - Quanto ganha motorista de uber")

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

        case _:
            print("Opção inválida.")
    
    print("")
    opcao_continuar = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_continuar == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")