#Recebe a quantidade de eleitores e calcule quem ganhou de 3 candidatos 

eleitores=int(input("digite a quantidade de eleitores: "))
candidato1=0
candidato2=0
candidato3=0

for i in range (eleitores):
    while True:
        voto=int(input("Digite o numero do candidato (1, 2 ou 3): "))
        if voto == 1:
            candidato1 += 1
            break
        elif voto == 2:
            candidato2 += 1
            break
        elif voto == 3:
            candidato3 += 1
            break
        else:
            print("Numero invalido, Tente novamente!")

print("Votação encerada!")
if candidato1 > candidato2:
    if candidato1> candidato3:
        print("O candidato 1 foi eleito")
    else:
        print ("O candidato 3 foi eleito")
elif candidato2 > candidato1:
    if candidato2> candidato3:
        print("O candidato 1 foi eleito")
    else:
        print ("O candidato 3 foi eleito")