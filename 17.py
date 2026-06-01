#informar codigo, altura e peso dos alunos
#encerar ao digitar codigo 0

contador=0
soma_altura = 0
soma_peso = 0 
mais_alto = 0
mais_baixo = 0
mais_gordo = 0
mais_magro = 0

cod_alto = 0
cod_baixo = 0
cod_magro = 0
cod_gordo = 0

while True:
    codigo = int(input("Digite o código do cliente(0 para sair): "))

    if codigo == 0:
        break

    altura = float(input("Digite a altura em metros: "))
    peso = float(input("Digite o peso: "))

    contador += 1 
    soma_altura += altura
    soma_peso += peso

    if contador == 1:
        mais_alto = altura
        mais_baixo = altura
        mais_gordo = peso
        mais_magro = peso

        cod_alto = codigo
        cod_baixo = codigo
        cod_gordo = codigo
        cod_magro = codigo

    if altura > mais_alto:
        mais_alto = altura
        cod_alto = codigo

    if altura < mais_baixo:
        mais_baixo = altura
        cod_baixo = codigo

    if peso > mais_gordo:
        mais_gordo = peso
        cod_gordo = codigo

    if peso < mais_magro:
        mais_magro = peso
        cod_magro = codigo

media_altura = soma_altura / contador
media_peso = soma_peso / contador

print(f"mais alto: Código {cod_alto}, Altura: {mais_alto}")
print(f"mais baixo: Código {cod_baixo}, Altura: {mais_baixo}")

print(f"mais Gordo: Código {cod_gordo}, Peso: {mais_gordo}")
print(f"mais Magro: Código {cod_magro}, Peso: {mais_magro}")

print(f"Média das alturas: {media_altura:.2f}")
print(f"Média de peso: {media_peso:.2f}")
