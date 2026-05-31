#calcula a média de N notas

num_notas=int(input("Quantas notas deseja adicionar: "))
quantidade=0
total=0

for i in range(num_notas):
    nota=float(input("Digite a nota: "))
    quantidade+=1
    total+=nota

media=total/quantidade
print("A média é: ",media )
