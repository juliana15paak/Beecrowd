n1, n2, n3, n4 = input().split()
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)
media = (n1*2 + n2*3 + n3*4 + n4*1) / 10
print(f"Media: {media:.1f}")
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    media = (media + exame) / 2
    if media > 5.0:
        print("Aluno aprovado.")
    elif media <= 4.9:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")
