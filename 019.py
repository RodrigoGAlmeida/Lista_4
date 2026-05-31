

for i in range(10):
    numero = int(input("Digite o número do aluno: "))
    altura = int(input("Digite a altura (cm): "))

    if i == 0:
        maior_altura = altura
        menor_altura = altura

        aluno_alto = numero
        aluno_baixo = numero

    if altura > maior_altura:
        maior_altura = altura
        aluno_alto = numero

    if altura < menor_altura:
        menor_altura = altura
        aluno_baixo = numero

print("Aluno mais alto:")
print(f"Número: {aluno_alto}, Altura: {maior_altura} cm")
print("Aluno mais baixo:")
print(f'Número: {aluno_baixo}, Altura: {menor_altura} cm')