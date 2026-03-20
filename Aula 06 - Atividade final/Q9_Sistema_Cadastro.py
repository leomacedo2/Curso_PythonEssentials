idade = 0
sexo = ""
quantidade_homens = 0
quantidade_mulheres = 0
soma_idades = 0

for i in range(1, 6):
    print(f"\nDigite os dados da {i}º pessoa")
    idade = int(input("Idade: "))
    
    while sexo != "M" and sexo != "F":
        sexo = input("Sexo (M/F): ").upper() #.upper() para garantir que a letra seja maiuscula
        if sexo != "M" and sexo != "F": 
            print("Sexo inválido. Por favor, digite 'M' ou 'F'.")

    if sexo == "M":
        quantidade_homens += 1
    else:
        quantidade_mulheres += 1

    soma_idades += idade
    # Resetar a variavel para proxima interação
    sexo = ""

media_idade = soma_idades / 5
print("")
print(f"Quantidade de homens: {quantidade_homens}")
print(f"Quantidade de mulheres: {quantidade_mulheres}")
print(f"Média de idade do grupo: {media_idade:.2f}")
