compra = float(input("Digite o valor da compra: R$ "))
desconto = 0

if compra <= 100:
    desconto =  compra * 0.05 # 5%
    compra = compra - desconto
elif compra <= 500:
    desconto = compra * 0.10 # 10%
    compra = compra - desconto
else:
    desconto = compra * 0.15 # 15%
    compra = compra - desconto
print("")
print(f"O valor final da compra é: R$ {compra:.2f}")
print(f"O desconto aplicado foi de: R$ {desconto:.2f}")