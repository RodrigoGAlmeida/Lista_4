#Montar tabela de preço de 1 a 50 unidades
#valor unitario 1.99

quantidade = 1
valor = 1.99

print("Lojas Quase Dois - Tabela de preços")
for i in range (50):
    print(f"{quantidade} - {valor:.2f}")
    quantidade+=1
    valor+=1.99