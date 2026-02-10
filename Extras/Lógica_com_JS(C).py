continuar = True

while continuar:
    print("")
    print("Aplicando Lógica com JS(C) - Terceira lista")
    print("1 - Ler 10 numeros inteiros e exibir a soma de todos")
    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")
    match opcao:

        case "1":
            soma = 0
            for i in range(10):
                numero = int(input(f"Digite o {i+1}º número inteiro: "))
                soma += numero
            print(f"A soma dos números é: {soma}")

        case _:
            print("Opção inválida.")
    
    print("")
    opcao_continuar = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_continuar == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")
