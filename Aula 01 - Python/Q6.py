# Questão: Algoritmo para ler um numero e informar se é positivo ou negativo
# Questão extra classe.

# Entrada de dados
numero = int(input("Digite um numero: "))

# Operador lógido condicional
if (numero > 0) :
    print(f"{numero} é positivo")
elif (numero == 0) :
    print("O numero é zero")
else :
    print(f"{numero} é negativo")