continuar = True
while continuar :
    # Menu de questões
    print("")
    print("Questionário da Aula 5. Laço de repetição 'for'. Escolha uma opção: ")
    print("1 - Algoritmo que imprime numeros de 1 a 50")
    print("2 - Numeros pares de 2 até 100")
    print("3 - Tabuada do 7")
    print("4 - Soma dos numeros de 1 a 20")
    print("5 - Numeros impares de 1 a 99")    
    print("6 - Imprima quadrados dos numeros de 1 a 15")
    print("7 - Algoritmo que vai de 100 até 1, imprimindo de 5 em 5")
    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")

    match opcao:

        case "1":
            for i in range(1,51):
                print(i)
        
        case "2":
            for i in range(1,101):
                if i % 2 == 0:
                    print(i)
        
        case "3":
            for i in range(1, 11):
                print(f"7 x {i} = {i*7}")

        case "4":
            soma = 0
            for i in range(1, 21):
                soma = soma + i
                print(soma)
            print(f"A soma dos numeros de 1 a 20 é {soma}")
        
        case "5":
            for i in range(0, 100):
                if i % 2 != 0:
                    print(i)
        
        case "6":
            for i in range(1,16):
                print(f"{i} ao quadrado é: {i*i}")
        
        case "7":
            for i in range(100, 0, -5):
                print(i)

        case _:
            print("Opção invalida!")
    
    print("")
    opcao_nova = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_nova == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")