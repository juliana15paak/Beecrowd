n, k = map(int, input().split())
alunos = []
while n > 0:
    nome_aluno = input()
    alunos.append(nome_aluno)
    n -= 1
alunos.sort()
print(alunos[k-1])
