def processar_conversao():
    # Técnica de escalabilidade: mude apenas este número
    TOTAL_MATERIAIS = 10 
    
    while True:
        # Criamos o dicionário com base no total definido
        materiais = {i: 0 for i in range(1, TOTAL_MATERIAIS + 1)}
        
        print("\n--- Início da Conversão ---")
        materiais[1] = int(input("Digite o valor do material 1: "))
        materiais[2] = int(input("Digite o valor do material 2: "))

        # Percorre os materiais para converter
        for i in range(1, TOTAL_MATERIAIS):
            # Realiza a conversão de 5 para 1
            if materiais[i] >= 1000:
                while materiais[i] >= 1000:
                    materiais[i] -= 5
                    materiais[i+1] += 1
                
                # Se o próximo transbordar e não for o último da lista
                if materiais[i+1] >= 1000 and (i + 1) < TOTAL_MATERIAIS:
                    # AQUI ESTÁ O QUE VOCÊ QUERIA: 
                    # Exibir todos os materiais convertidos até agora
                    print("\n" + "="*20)
                    for m in range(1, i + 1):
                        print(f"Valor do material {m}: {materiais[m]}")
                    print(f"Valor PARCIAL do material {i+1}: {materiais[i+1]}")
                    print("="*20)
                    
                    # Pede o próximo valor
                    proximo = i + 2
                    materiais[proximo] = int(input(f"\nDigite o valor do material {proximo}: "))
                else:
                    # Se não transbordou, encerra o loop de inputs
                    break
            else:
                # Se o material atual não atingiu 1000, para a cadeia
                break

        # Exibição do Resultado Final (todos que foram mexidos)
        print("\n--- Resultados Finais ---")
        for i in range(1, TOTAL_MATERIAIS + 1):
            # Só mostra até o material que recebeu algum valor
            if materiais[i] > 0 or i <= 2:
                print(f"Valor do material {i}: {materiais[i]}")

        opcao = input("\nDeseja continuar? Digite 'n' para encerrar: ").lower()
        if opcao == 'n':
            break

if __name__ == "__main__":
    processar_conversao()