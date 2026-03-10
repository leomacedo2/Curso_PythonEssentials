continuar = True
while continuar :
    # Menu de questões
    print("")
    print("Questionário da Aula 5. Laço de repetição 'while'. Escolha uma opção: ")
    print("1 - Ler numeros até o usuario digitar um valor negativo")
    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")

    match opcao:

        case "1":
            num = 0
            while num >= 0:
                num = int(input("Digite um numero (digite um valor negativo para encerrar): "))
                if num >= 0:
                    print(f"Você digitou: {num}")
                else:
                    print("Valor negativo digitado. Encerrando o programa.")

        case _:
            print("Opção invalida!")
    
    print("")
    opcao_nova = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_nova == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")