while True:
    try:
        epr, ehd, intrusos = 0, 0, 0
        num_alunos = int(input())
        
        while num_alunos > 0:
            matricula, curso = input().split()
            if curso == 'EPR':
                epr += 1
            elif curso == 'EHD':
                ehd += 1
            else:
                intrusos += 1
            num_alunos -= 1

        print("EPR:",epr)
        print("EHD:",ehd)
        print("INTRUSOS:",intrusos)
    except EOFError:
        break
