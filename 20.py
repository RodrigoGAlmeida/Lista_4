maior_indice=0
menor_indice=99999999999999
cid_maior = ""
cid_menor = ""
soma_veiculos = 0
soma_acidentes_menos_2000 = 0
contador_cid_menos_2000 = 0

for i in range (5):
    print("Cidade",i+1)
    
    codigo=input("Digite o codigo da cidade: ")
    veiculos = int(input("Numero de veiculos de passeio: "))
    acidente = int(input("Numero de acidentes com vitimas: "))
    indice = acidente / veiculos

    if indice > maior_indice:
        maior_indice = indice
        cid_maior = codigo

    if indice < menor_indice:
        menor_indice = indice
        cid_menor = codigo

    soma_veiculos += veiculos

    if veiculos < 2000:
        soma_acidentes_menos_2000 += acidente
        contador_cid_menos_2000 += 1

media_veiculos = soma_veiculos / 5

if contador_cid_menos_2000 > 0:
    media_acidentes = (soma_acidentes_menos_2000 / contador_cid_menos_2000)

else:
    media_acidentes = 0

print(f"maior indice de acidentes: {maior_indice:.4f}")
print("Cidade: ",cid_maior)

print(f"menor indice de acidentes:{menor_indice:.4f}")
print("Cidade: ",cid_menor)

print(f"Media de veiculos nas 5 cidades: {media_veiculos:.2f}")

print(f"Media de acidentes nas cidades com menos de 2000 veiculos: {media_acidentes:.2f}")
