largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
litros_necessarios = area / 2 #1 litro pinta 2 metros quadrados
print("")
print(f"Serão necessários {litros_necessarios:.2f} litros de tinta para pintar a parede numa area de {area:.2f} metros quadrados.")