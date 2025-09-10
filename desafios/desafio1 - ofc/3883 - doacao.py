soma = 0

while True:
    doacao_vc = float(input())
    if doacao_vc == -1:
        break
    else:
        soma += doacao_vc
        
total_reais = soma * 2.5
print(f"VC$ {soma:.2f}")
print(f"R$ {total_reais:.2f}")
