#calcule o gasto total pelo colecionador de cd
#Calcule o gasto medio por CD

quantidade=int(input("Digite a quantidades de CD's na coleção: "))
total=0
for i in range(quantidade):
    preco=float(input(f"Digite o valor do CD {i+1}: "))
    total+=preco

media=total/quantidade
print("O gasto total foi: R$", total)
print("O gasto médio por CD foi de: R$", media)
