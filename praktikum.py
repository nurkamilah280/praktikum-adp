nama = input('masukkan nama anda : ')
umur = input('masukkan umur anda : ')
jenis_kelamin = input('jenis kelamin (Pria/Wanita) : ')
print('tiket dan tujuan yang tersedia : ') 
print('kode maskapai : 3012, tujuan : Padang-Jakarta')
print('Ekonomi : Rp.800.000,00, Bisnis : Rp.850.000,00, First Class : Rp.900.000')
print('kode maskapai : 4015, tujuan : Padang-Batam')
print('Ekonomi : Rp.500.000,00, Bisnis : Rp.550.000,00, First Class : Rp.700.000')
print('kode maskapai : 3012, tujuan : Padang-Bandung')
print('Ekonomi : Rp.700.000,00, Bisnis : Rp.750.000,00, First Class : Rp.850.000')
kode_maskapai = input('tulis kode maskapai pilihan : ')
jenis_maskapai = input('pilih jenis maskapai (Ekonomi/Bisnis/First Class) : ')
if kode_maskapai == '3012'  and jenis_maskapai == 'ekonomi' :
    tujuan_penerbangan = 'Padang-Jakarta'
    harga = 800000
elif kode_maskapai == '3012'  and jenis_maskapai == 'bisnis' :
    tujuan_penerbangan = 'Padang-Jakarta'
    harga = 850000
elif kode_maskapai == '3012'  and jenis_maskapai == 'first class' :
    tujuan_penerbangan = 'Padang-Jakarta'
    harga = 900000
elif kode_maskapai == '4015' and jenis_maskapai == 'ekonomi' :
    tujuan_penerbangan = 'Padang-Batam'
    harga = 500000
elif kode_maskapai == '4015' and jenis_maskapai == 'bisnis' :
    tujuan_penerbangan = 'Padang-Batam'
    harga = 550000
elif kode_maskapai == '4015' and jenis_maskapai == 'first class' :
    tujuan_penerbangan = 'Padang-Batam'
    harga = 700000
elif kode_maskapai == '4050' and jenis_maskapai == 'ekonomi' :
    tujuan_penerbangan = 'Padang-Bandung'
    harga = 700000
elif kode_maskapai == '4050' and jenis_maskapai == 'bisnis' :
    tujuan_penerbangan = 'Padang-Bandung'
    harga = 750000
elif kode_maskapai == '4050' and jenis_maskapai == 'first Class' :
    tujuan_penerbangan = 'Padang-Bandung'
    harga = 850000
else :
    kode_maskapai = 'terjadi kesalahan pada kode yang anda inputkan'
jenis_maskapai = jenis_maskapai
kode_maskapai = kode_maskapai
jumlah_tiket = int(input('jumlah kursi yang akan dipesan : '))
if jumlah_tiket > 3 :
    total_harga = harga*jumlah_tiket*20/100
else :
    total_harga = harga*jumlah_tiket
print('nama                 : ',nama)
print('umur                 : ',umur)
print('jenis kelamin        : ',jenis_kelamin)
print('tujuan penerbangan   : ',tujuan_penerbangan)
print('kode maskapai        : ', kode_maskapai)
print('jenis maskapai       : ', jenis_maskapai)
print('harga satuan         : ',harga)
print('jumlah tiket         : ',jumlah_tiket)
print('total harga          : ',total_harga)