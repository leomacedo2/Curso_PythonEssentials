continuar = True
while continuar :
    # Menu de questões
    print("")
    print("Questionário da Aula 5. Laço de repetição 'while'. Escolha uma opção: ")
    print("1 - Ler numeros até o usuario digitar um valor negativo")
    print("2 - Lendo notas de alunos enquanto ela for valida (entre 0 e 10)")
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

        case "2":
            nota = -1
            while nota < 0 or nota > 10:
                nota = float(input("Digite uma nota entre 0 e 10: "))
                if nota < 0 or nota > 10:
                    print("Nota inválida. Programa encerrado.")
                else:
                    print(f"Nota de aluno: {nota:.2f}")
            
        case _:
            print("Opção invalida!")
    
    print("")
    opcao_nova = input("Deseja ver outra questão? Digite 'n' para encerrar: ")

    if opcao_nova == "n":
        continuar = False
        print("")
        print("Obrigado!")
        print("")