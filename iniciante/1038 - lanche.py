cod, qtd = map(int, (input()).split())

match(cod):
    case 1:
        preco = 4.0*qtd
        print(f"Total: R$ {preco:.2f}")
    case 2:
        preco = 4.5*qtd
        print(f"Total: R$ {preco:.2f}")
    case 3:
        preco = 5.0*qtd
        print(f"Total: R$ {preco:.2f}")
    case 4:
        preco = 2.0*qtd
        print(f"Total: R$ {preco:.2f}")
    case 5:
        preco = 1.5*qtd
        print(f"Total: R$ {preco:.2f}")
        
