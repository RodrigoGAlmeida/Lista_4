#recebe a quantidade de turmas e quantos alunos tem por turma e faz a media
#a turma não pode ter mais de 40 alunos

qnt_turmas=int(input("Digite a quantidade de turmas: "))
alunos = 0

for i in range(qnt_turmas):
    while True:
        aln_turma = int(input(f"Digite a quantidade de alunos na turma {i+1}: "))
        if 0 <= aln_turma <= 40:
            alunos += aln_turma
            break
        else:
            print("Número inválido, o máximo de alunos por turma é 40")
            print("Tente novamente!")

media = alunos / qnt_turmas
print("A média de alunos por turma é:", media)