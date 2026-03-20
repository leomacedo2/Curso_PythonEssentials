num = 0
for i in range(1, 21):
    num = num + float(input(f"Digite o {i}º número: "))
media = num / 20
print("")
print(f"A média Final é: {media:.2f}")