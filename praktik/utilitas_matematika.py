def luas_persegi_panjang(p, l):
    return p * l
print(luas_persegi_panjang(8, 5))

def luas_segitiga(a, t):
    return 0.5 * a * t
print(luas_segitiga(10, 6))

def jumlah_n(n):
    total = 0
    for i in range(1, n + 1) :
        total += i
    return total
print(jumlah_n(10))

def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil
print(faktorial(5))

def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil
print(faktorial(0))

def tampilkan_menu():
    print("1. luas persegi panjang")
    print("2. luas segitiga")
    print("3. jumlah 1 sampai n")
    print("4. faktorial")