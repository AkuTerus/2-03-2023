def selisih_hari(tanggal1,bulan1,tanggal2,bulan2):
    jumlah_hari = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    hari_dalam_tahun=sum(jumlah_hari)
    tanggal_pertama=sum(jumlah_hari[bulan1:])-tanggal1
    tanggal_kedua=sum(jumlah_hari[:bulan2])+tanggal2
    selisih=hari_dalam_tahun-tanggal_pertama-tanggal_kedua
    print(abs(selisih))


tanggal1=int(input('tanggal pertama:'))
bulan1=int(input('bulan pertama:'))
tanggal2=int(input('tanggal kedua:'))
bulan2=int(input('bulan keduaL '))

selisih_hari(tanggal1,bulan1,tanggal2,bulan2)


