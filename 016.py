#montar tabuadada do valor informado
#Usuario informa inicio e fim

multiplicando=int(input("Digite o valor da tabuada: "))
inicio=int(input("Digite o valor inicial da tabuada: "))
final=int(input("Digite o valor final da tabuada: " ))

while final<inicio:
    print("O valor final não pode ser menor que o inicial!")
    inicio=int(input("Digite o valor inicial da tabuada: "))
    final=int(input("Digite o valor final da tabuada" ))

print(f"Vou montar a tabuada de {multiplicando} começando em {inicio} e terminando em {final}:")
for i in range (inicio, final+1):
    resultado= multiplicando * i
    print(multiplicando, "X",i,"=",resultado)