num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# para o calculo da Raiz cúbica, basta elevar o produto dos números a 1/3
media_geometrica = (num1 * num2 * num3) ** (1/3)
print("")
print(f"A média geométrica dos números {num1}, {num2} e {num3} é: {media_geometrica:.2f}")