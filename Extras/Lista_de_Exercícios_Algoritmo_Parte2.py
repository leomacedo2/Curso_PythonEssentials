continuar = True

while continuar:
    print("")
    print("Lista de Exercícios Parte 2 - Algoritmo")
    print("1 - Conversão de Dolares para Reais")
    print("2 - Quanto ganha motorista de uber")
    print("3 - Identificar se é par ou impar")
    print("4 - Ler 10 cidades em uma unica variavel")
    print("5 - Ler 10 carros, placas e valores de diarias em uma unica variavel")
    print("6 - Ler maioridade")
    print("7 - Positivo ou negativo")
    print("8 - Lista de Funcionários")
    print("9 - Triângulo retângulo")
    print("10 - Numeros em ordem crescente")

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
            print(cidades.strip(", "))

        case "5":
            carros = ""
            for i in range(1, 11):
                carros = carros + "\nCarro " + str(i) + ": " + input(f"Digite o nome do carro {i}: ") + ", "
                carros = carros + "Placa: " + input(f"Digite a placa do carro {i}: ") + ", "
                carros = carros + "Valor: " + "R$ " + str(float(input(f"Digite o valor da diaria do carro {i}: R$ ")))
            print("\nOs carros lidos foram:")
            print(carros)

        case "6":
            idade = int(input("Digite a idade: "))
            if idade >= 18:
                print("É maior de idade!")
            else:
                print("É menor de idade!")
        
        case "7":
            num = float(input("Digite um valor: "))
            if num > 0:
                print(f"O valor {num} é positivo")
            elif num < 0:
                print(f"O valor {num} é negativo")
            else:
                print("O valor é zero")
        
        case "8":
            nomes_funcoes = ""
            idades_salarios = ""

            for i in range(1, 3):
                print(f"\n--- Digite os dados do {i}º funcionário")
                
                nome = input("Nome: ")
                funcao = input("Função: ")
                idade = int(input("Idade: "))
                salario = float(input("Salário: R$ "))

                if idade > 25:
                    # 20% é igual a multiplicar por 1.20
                    salario = salario * 1.20 

                nomes_funcoes = nomes_funcoes + f"[{i}] {nome} - {funcao}\n"
                
                idades_salarios = idades_salarios + f"[{i}] {idade} anos - R$ {salario:.2f}\n"

            print("\n=== Lista de Funcionários: ===")
            print("\n[ Nomes e Funções ]")
            print(nomes_funcoes)
            
            print("[ Idades e Salários ]")
            print(idades_salarios)
        
        case "9":
            base = float(input("Digite o valor da base do triângulo: "))
            altura = float(input("Digite o valor da altura do triângulo: "))

            area = base*altura / 2

            print(f"A area do triângulo é {area:.2f}")
        
        case "10":
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
            num3 = int(input("Digite o terceiro numero: "))

            if num1 < num2 and num2 < num3:
                print(f"Os numeros em ordem crescente são: {num1}, {num2}, {num3}")
            elif num1 < num3 and num3 < num2:
                print(f"Os numeros em ordem crescente são: {num1}, {num3}, {num2}")
            elif num2 < num1 and num1 < num3:
                print(f"Os numeros em ordem crescente são: {num2}, {num1}, {num3}")
            elif num2 < num3 and num3 < num1:
                print(f"Os numeros em ordem crescente são: {num2}, {num3}, {num1}")
            elif num3 < num1 and num1 < num2:
                print(f"Os numeros em ordem crescente são: {num3}, {num1}, {num2}")
            else:
                print(f"Os numeros em ordem crescente são: {num3}, {num2}, {num1}")
            
        case _:
            print("Opção inválida.")
    
    print("")
    opcao_continuar = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_continuar == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")