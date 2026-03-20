soma5 = 0
soma3 = 0
print("Números múltiplos de 5:")
for i in range(1, 151):
    if i % 5 == 0:
        print(i, end=" ")
        soma5 += i
print(f"\nSoma dos múltiplos de 5: {soma5}")
print("\nNúmeros múltiplos de 3:")
for i in range(1, 151):
    if i % 3 == 0:
        print(i, end=" ")
        soma3 += i
print(f"\nSoma dos múltiplos de 3: {soma3}")
print(f"\nSoma total: {soma3 + soma5}")
