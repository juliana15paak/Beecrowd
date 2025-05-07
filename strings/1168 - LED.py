caso_testes = int(input())
while caso_testes > 0:
    n = input()
    i = 0
    soma = 0
    while i < len(n):
        if n[i] == '1':
            soma += 2
        elif n[i] == '2':
            soma += 5
        elif n[i] == '3':
            soma += 5
        elif n[i] == '4':
            soma += 4
        elif n[i] == '5':
            soma += 5
        elif n[i] == '6':
            soma += 6
        elif n[i] == '7':
            soma += 3
        elif n[i] == '8':
            soma += 7
        elif n[i] == '9':
            soma += 6
        elif n[i] == '0':
            soma += 6
        i += 1
    print(soma,'leds')
    caso_testes -= 1

        
