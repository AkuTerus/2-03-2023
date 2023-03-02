def jumlah_hari(nama_bulan):
    bulan_31_hari=['januari','maret','mei','juli','agustus','oktober','desember']
    bulan_28_hari=['februari']
    bulan_30_hari=['april','juni','september','november']
    if nama_bulan in bulan_31_hari:
        print('31 Hari')
    elif nama_bulan in bulan_28_hari:
        print('28 Hari')
    elif nama_bulan in bulan_30_hari:
        print('30 Hari')
    else:print('Tidak Valid')

nama_bulan=input('Masukan Nama Bulan:')
nama_bulan=nama_bulan.lower()
jumlah_hari(nama_bulan)