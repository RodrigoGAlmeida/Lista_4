#calcula a média de idade de N notas alunos

num_alunos = int(input("Quantos alunos deseja adicionar: "))
quantidade = 0
total = 0
aluno = 1

for i in range(num_alunos):
    idade = float(input(f"Digite a idade do aluno {aluno}: "))
    quantidade += 1
    total += idade
    aluno += 1

media = total / quantidade
print("A média é:", media )

if media < 26:
    print('Turma jovem')
elif media < 61:
    print('Turma adulta')
else:
    print("Turma velha")