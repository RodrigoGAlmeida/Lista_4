#montar tabela de pães
#valor unitario 0.18

quantidade = 1
valor = 0.18

print("Preço do pão: R$ 0.18")
print("Panificadora Pão de Ontem - Tabela de preços")
for i in range (50):
    print(f"{quantidade} - {valor:.2f}")
    quantidade+=1
    valor+=0.18