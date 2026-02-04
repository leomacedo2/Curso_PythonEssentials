continuar = True

while continuar:
    print("")
    print("Aplicando Lógica com JS(B) - Primeira lista")
    print("1 - Calculo de área de terreno")
    print("2 - Quantidade de ferraduras compradas para um haras")
    print("3 - Terça parte de um numero dado")
    print("4 - Dobro e o triplo de um numero")
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

            
        case _:
            print("Opção inválida.")
    
    print("")
    opcao_continuar = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_continuar == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")
