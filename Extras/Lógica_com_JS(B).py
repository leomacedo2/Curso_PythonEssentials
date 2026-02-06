continuar = True

while continuar:
    print("")
    print("Aplicando Lógica com JS(B) - Segunda lista")
    print("1 - Calculo de área de terreno")
    print("2 - Quantidade de ferraduras compradas para um haras")
    print("3 - Terça parte de um numero dado")
    print("4 - Dobro e o triplo de um numero")
    print("5 - Volume de uma caixa d'água cilíndrica")
    print("6 - Conversão de valor de metros para cm, mm e km")
    print("7 - Viagens de um motorista de Uber")
    print("8 - Área de um triângulo retângulo lendo seus lados")
    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")
    match opcao:


        case "1":
            largura = float(input("Digite a largura do terreno: "))
            comprimento = float(input("Digite o comprimento do terreno: "))
            area = largura * comprimento
            print(f"A área do terreno é: {area} m²")


        case "2":
            cavalos = int(input("Digite a quantidade de cavalos no haras: "))
            ferraduras = cavalos * 4
            print(f"A quantidade de ferraduras necessárias é: {ferraduras}")

        
        case "3":
            numero = float(input("Digite um número real qualquer: "))
            terca_parte = numero / 3
            print(f"A terça parte do número é: {terca_parte}")

        
        case "4":
            numero = float(input("Digite um número: "))
            dobro = numero * 2
            triplo = numero * 3
            print(f"O dobro do número é: {dobro}")
            print(f"O triplo do número é: {triplo}")

        
        case "5":
            import math
            raio = float(input("Digite o raio da base da caixa d'água (em metros): "))
            altura = float(input("Digite a altura da caixa d'água (em metros): "))
            volume = math.pi * (raio ** 2) * altura
            print(f"O volume da caixa d'água é: {volume:.2f} metros cúbicos")


        case "6":
            metros = float(input("Digite o valor em metros: "))
            centimetros = metros * 100
            milimetros = metros * 1000
            quilometros = metros / 1000
            print("")
            print(f"{metros} metros equivalem a:")
            print(f"{centimetros} centímetros")
            print(f"{milimetros} milímetros")
            print(f"{quilometros} quilômetros")

        
        case "7":
            viagens = int(input("Digite o número de viagens realizadas: "))
            total_ganho = viagens * 6.80
            print(f"O total ganho pelo motorista de Uber é: R$ {total_ganho:.2f}")

        
        case "8":
            lado1 = float(input("Digite o valor do primeiro lado do triângulo retângulo: "))
            lado2 = float(input("Digite o valor do segundo lado do triângulo retângulo: "))
            area = (lado1 * lado2) / 2
            print(f"A área do triângulo retângulo é: {area}")


        case _:
            print("Opção inválida.")
    
    print("")
    opcao_continuar = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_continuar == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")
