# Criamos uma função só para validar a entrada do usuário
def obter_numero_valido(mensagem):
    while True:
        try:
            # Tenta converter o texto digitado para um número inteiro
            return int(input(mensagem))
        except ValueError:
            # Se der erro (ValueError), avisa e o loop 'while True' repete a pergunta
            print("⚠️ Erro: Por favor, digite apenas números. Letras ou símbolos não são aceitos.")

def processar_conversao():
    TOTAL_MATERIAIS = 10 
    
    while True:
        materiais = {i: 0 for i in range(1, TOTAL_MATERIAIS + 1)}
        materiais_iniciais = {i: 0 for i in range(1, TOTAL_MATERIAIS + 1)}
        
        print("\n--- Início da Conversão ---")
        
        # Substituímos o 'int(input(...))' pela nossa nova função de segurança
        materiais[1] = obter_numero_valido("Digite o valor do material 1: ")
        materiais_iniciais[1] = materiais[1]
        
        materiais[2] = obter_numero_valido("Digite o valor do material 2: ")
        materiais_iniciais[2] = materiais[2]

        for i in range(1, TOTAL_MATERIAIS):
            if materiais[i] >= 1000:
                while materiais[i] >= 1000:
                    materiais[i] -= 5
                    materiais[i+1] += 1
                
                if materiais[i+1] >= 1000 and (i + 1) < TOTAL_MATERIAIS:
                    print("\n" + "="*20)
                    for m in range(1, i + 1):
                        print(f"Valor do material {m}: {materiais[m]}")
                    print(f"Valor PARCIAL do material {i+1}: {materiais[i+1]}")
                    print("="*20)
                    
                    proximo = i + 2
                    # Usamos a função de segurança aqui também!
                    materiais[proximo] = obter_numero_valido(f"\nDigite o valor do material {proximo}: ")
                    materiais_iniciais[proximo] = materiais[proximo]
                else:
                    break
            else:
                break

        print("\n--- Resultados Finais ---")
        for i in range(1, TOTAL_MATERIAIS + 1):
            if materiais_iniciais[i] > 0 or materiais[i] > 0 or i <= 2:
                print(f"Valor do material {i}: {materiais_iniciais[i]} -> {materiais[i]}")

        opcao = input("\nDeseja continuar? Digite 'n' para encerrar: ").lower()
        if opcao == 'n':
            break

if __name__ == "__main__":
    processar_conversao()