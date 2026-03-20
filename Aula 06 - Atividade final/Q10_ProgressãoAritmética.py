pa_1 = int(input("Digite o primeiro termo da progressão aritmética: "))
pa_razao = int(input("Digite a razão da progressão aritmética: "))
n = int(input("Digite qual termo deseja calcular: "))
pa_n = pa_1 + (n - 1) * pa_razao
print("")
print(f"O {n}º termo da progressão aritmética é: {pa_n}")
