continuar = True

while continuar:
    print("")
    print("Lista de Exercícios - Algoritmo")
    print("1 - Atribuição de variáveis")
    print("")
    opcao = input("Qual resposta quer ver? Digite o numero: ")
    print("")
    
    match opcao:

        case "1":
            nome = "Leo"
            idade = 34
            altura = 1.75
            print(f"Nome: {nome}")
            print(f"Idade: {idade} anos")
            print(f"Altura: {altura} metros")

        case _:
            print("Opção inválida.")
    
    print("")
    opcao_continuar = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_continuar == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")