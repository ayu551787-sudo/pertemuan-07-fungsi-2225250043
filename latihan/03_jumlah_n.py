def jumlah_n(n):
    total = 0
    for i in range(1,int(n) + 1) :
        total += i
    return n * (n + 1) // 2
print(jumlah_n(100))


def jumlah_n(n):
    total = 0
    for i in range(1, n + 1) :
        total += i
    return total
print(jumlah_n(100))

