qtd_dias = int(input())

def membro(codigo):
    match(codigo):
        case 1: print("Rolien")
        case 2: print("Naej")
        case 3: print("Elehcim")
        case 4: print("Odranoel")
        
while qtd_dias > 0:
    qtd_feedbacks = int(input())
    while qtd_feedbacks > 0:
        cod = int(input())
        membro(cod)
        qtd_feedbacks -= 1
    qtd_dias -= 1

