estoque_inicial = int(input("Digite a quantidade inicial de um produto em estoque: "))
quantidade_vendida = int(input("Digite a quantidade desse produto que foram vendidos: "))
quantidade_comprada = int(input("Digite a quantidade desse produto que foram comprados: "))
estoque_final = estoque_inicial - quantidade_vendida + quantidade_comprada
print("")
if estoque_final < 10:
    print(f"Estoque final: {estoque_final} - Necessário comprar mais produtos.")
else:
    print(f"Estoque final: {estoque_final} - Estoque OK.")