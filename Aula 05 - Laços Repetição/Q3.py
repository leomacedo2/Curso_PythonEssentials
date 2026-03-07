# Crie um algoritmo que apresente a quantidade de números pares 
# e de numeros ímpares, enquanto o usuário digitar um valor diferente de 0

num = int(input("Digite um valor: "))
pares = 0
impares = 0

while num != 0:
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    num = int(input("Digite outro valor(0 para encerrar): "))

print("")
print(f"A quantidade de numeros pares é: {pares}")
print(f"A quantidade de numeros impares é: {impares}")

