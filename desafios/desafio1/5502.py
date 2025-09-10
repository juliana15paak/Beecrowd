valor, max_meses, valor_resgate = input().split()
valor_min, temp, porcentagem = input().split()
valor, max_meses, valor_resgate = float(valor),int(max_meses),float(valor_resgate)
valor_min, temp, porcentagem = float(valor_min),int(temp),float(porcentagem)

if valor >= valor_min:
    if temp <= max_meses:
        aplicacao = valor * porcentagem * max_meses / 100
        if aplicacao >= valor_resgate:
            print("invista!")
        else:
            print("nao invista!")
    else:
        print("nao invista!")
else:
    print("nao invista!")
