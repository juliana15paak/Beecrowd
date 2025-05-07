while True:
    d, n = input().split()

    if d == '0' and n == '0':
        break

    v = n.replace(d, '')
    v = v.lstrip('0')

    if v == '':
        print(0)
    else:
        print(v)
