l_capital_inicial, l_tempo_max, l_valor_final_min = input().split()
p_capital_inicial_min, p_tempo_min, p_porcentagem = input().split()

l_capital_inicial = float(l_capital_inicial)
l_tempo_max, p_tempo_min = int(l_tempo_max), int(p_tempo_min)
l_valor_final_min = float(l_valor_final_min )

p_capital_inicial_min = float(p_capital_inicial_min)
p_porcentagem = float(p_porcentagem)

if p_tempo_min > l_tempo_max or l_capital_inicial < p_capital_inicial_min:
    print("nao invista!")
else:
    final = l_capital_inicial + p_porcentagem / 100 * l_capital_inicial
    if final < l_valor_final_min:
        print("nao invista!")
    else:
        print("invista!")
