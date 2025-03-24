while True :
    print('>>>>>>>>>> Selamat Datang <<<<<<<<<<')
    nama = input('Siapa nama anda ?\n')
    mulai =input('Tekan p untuk memulai atau tombol lain untuk berhenti \n')
    if mulai == 'p' :
        print(f'Terima kasih telah memilih layanan kami')
        break
    else :
        print(f'Terima kasih {nama}, sampai jumpa kembali!')
#Input jumlah baris dan kolom kursi bioskop
while True :   
    r = int(input('masukkan jumlah baris kursi bioskop : '))
    c = int(input('masukkan jumlah kolom kursi bioskop : '))
    if r < 4 :
        print('ukuran minimum kursi biokop adalah 4x4!')
    elif c < 4 :
        print('ukuran minimum kursi bioskop adalah 4x4!')
    else :
        break
#Layout kursi bioskop
m = r*c
for i in range (1,m+1) :
    if i % c == 0 :
        print(i)
    else :
        print(f'{i} ', end = '\t')
#Pemilihan kursi oleh pengguna
kursi_terpesan = set( )
while True :
    n = int(input('masukkan nomor kursi yang akan dipesan : ')) 
    if n > m :
        print('kursi yang anda pilih tidak tersedia')
    elif n == 0 :
        print('terima kasih sudah berkunjung!')
        break
    else : 
        kursi_terpesan.add(n)  
        print(f'kursi {n} berhasil dipesan!')
    for i in range (1,m+1) :
        if i in kursi_terpesan: 
            print('X', end = '\t')
            if i % c == 0 :
                print( )
            continue
        print(f'{i} ', end = '\t')
        if i % c == 0 :
            print( )