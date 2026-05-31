# Recebe quantidade indeterminada de temperaturas
# calcula média e menor valor

maior = 0
menor = 99999
total = 0
contagem = 0
continuar = True

while continuar:
    temp = int(input("Digite a Temperatura: "))
    total += temp
    contagem += 1
    if temp < menor:
        menor = temp
    if temp > maior:
        maior = temp

    while True:
        resposta = input("Deseja adicionar outro valor (S/N): ").upper()
        if resposta == "S":
            continuar = True
            break
        elif resposta == "N":
            continuar = False
            break
        else:
            print("resposta Invalida!")

media = total / contagem
print("Média das temperaturas: ", media)
print("Menor temperatura: ", menor)
print("Maior temperatura: ", maior)
