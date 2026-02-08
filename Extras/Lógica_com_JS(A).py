continuar = True

while continuar:
    print("")
    print("Aplicando Lógica com JS(A) - Primeira lista")
    print("1 - Qual idade de uma pessoa?")
    print("2 - Calculo de volume de uma esfera")
    print("3 - Calculadora de 2 numeros")
    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")
    
    match opcao:
        case "1":
            ano = int(input("Digite seu ano de nascimento: "))
            idade = 2026 - ano
            print(f"A sua idade no final do ano de 2026 será: {idade}")
        

        case "2":
            import math
            raio = float(input("Digite o raio da esfera (em metros): "))
            volume = (4/3) * math.pi * (raio ** 3)
            print(f"O volume da esfera é: {volume:.2f} metros cúbicos")

        
        case "3":
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            print(f"A soma dos dois números é: {numero1 + numero2}")
            print(f"A subtração do primeiro número pelo segundo é: {numero1 - numero2}")
            print(f"A multiplicação dos dois números é: {numero1 * numero2}")
            if numero2 != 0:
                print(f"A divisão do primeiro número pelo segundo é: {numero1 / numero2}")
            else:
                print("Não é possível dividir por zero.")
        
        
        case _:
            print("Opção inválida.")
    
    print("")
    opcao_continuar = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_continuar == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")
