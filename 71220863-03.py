def rata_rata(n1,n2,n3,n4,n5,n6,n7,n8):
    nilai = [n1,n2,n3,n4,n5,n6,n7,n8]
    kecil = min(nilai)
    nilai.remove(kecil)
    kecil2 = min(nilai)
    nilai.remove(kecil2)
    print(kecil)
    print(kecil2)
    total = sum(nilai)
    rata2 = total//6
    print(round(rata2))
    

n1 = int(input('Masukan nilai 1 : '))
n2 = int(input('Masukan nilai 2 : '))
n3 = int(input('Masukan nilai 3 : '))
n4 = int(input('Masukan nilai 4 : '))
n5 = int(input('Masukan nilai 5 : '))
n6 = int(input('Masukan nilai 6 : '))
n7 = int(input('Masukan nilai 7 : '))
n8 = int(input('Masukan nilai 8 : '))
rata_rata(n1, n2, n3, n4, n5, n6, n7, n8)